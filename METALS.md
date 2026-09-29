# Gold & Silver Fair-Value Bot

*Updated Mon Sep 28, 8:20 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

⏳ **Too early.** 8 of 30 settled trades needed before judging.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 10 | 8 | 3 (38%) | 36¢ | 45% | -$0.32 | -1% |
| Silver | 5 | 4 | 1 (25%) | 34¢ | 42% | -$4.04 | -29% |
| Gold | 5 | 4 | 2 (50%) | 39¢ | 48% | $3.72 | +23% |

*Earlier half $15.15 / later half -$15.47.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 8 | 3 (38%) | -$3.16 | -10% |
| 4¢+ ← live bot | 8 | 3 (38%) | $3.78 | +14% |
| 6¢+ | 8 | 3 (38%) | $6.97 | +30% |
| 8¢+ | 8 | 4 (50%) | $19.60 | +96% |
| 10¢+ | 7 | 1 (14%) | -$2.92 | -23% |
| 15¢+ | 2 | 1 (50%) | $7.32 | +273% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 196 | -2.3% |
| Hyperliquid price vs Kalshi's target | 196 | +5.5% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 8:18:20 PM | Silver | DOWN | 11.7 min | 39¢ | 48% | 7¢ | Open | — |
| 9/28 8:17:38 PM | Gold | UP | 12.4 min | 45¢ | 51% | 5¢ | Open | — |
| 9/28 8:01:29 PM | Gold | UP | 13.5 min | 32¢ | 43% | 10¢ | ❌ Lost | -$3.36 |
| 9/28 8:01:07 PM | Silver | UP | 13.9 min | 42¢ | 48% | 4¢ | ❌ Lost | -$4.38 |
| 9/28 7:47:42 PM | Silver | UP | 12.3 min | 30¢ | 37% | 5¢ | ❌ Lost | -$3.15 |
| 9/28 7:46:12 PM | Gold | DOWN | 13.8 min | 44¢ | 51% | 5¢ | ❌ Lost | -$4.58 |
| 9/28 7:32:13 PM | Silver | UP | 12.8 min | 33¢ | 41% | 6¢ | ✅ Won | $6.54 |
| 9/28 7:31:57 PM | Gold | UP | 13.1 min | 35¢ | 45% | 8¢ | ✅ Won | $6.34 |
| 9/28 7:17:04 PM | Gold | UP | 12.9 min | 45¢ | 54% | 7¢ | ✅ Won | $5.32 |
| 9/28 7:17:00 PM | Silver | UP | 13.0 min | 29¢ | 41% | 11¢ | ❌ Lost | -$3.05 |
