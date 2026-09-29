# Gold & Silver Fair-Value Bot

*Updated Mon Sep 28, 9:30 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

⏳ **Too early.** 16 of 30 settled trades needed before judging.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 18 | 16 | 9 (56%) | 37¢ | 45% | $28.23 | +46% |
| Silver | 9 | 8 | 3 (38%) | 31¢ | 39% | $4.23 | +16% |
| Gold | 9 | 8 | 6 (75%) | 43¢ | 51% | $24.00 | +67% |

*Earlier half -$0.32 / later half $28.55.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 16 | 8 (50%) | $7.21 | +10% |
| 4¢+ ← live bot | 16 | 8 (50%) | $20.38 | +34% |
| 6¢+ | 16 | 7 (44%) | $20.72 | +42% |
| 8¢+ | 15 | 7 (47%) | $28.79 | +70% |
| 10¢+ | 14 | 4 (29%) | $10.82 | +37% |
| 15¢+ | 7 | 3 (43%) | $17.04 | +131% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 397 | +1.2% |
| Hyperliquid price vs Kalshi's target | 397 | +3.1% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 9:18:13 PM | Gold | DOWN | 11.8 min | 35¢ | 42% | 6¢ | Open | — |
| 9/28 9:16:07 PM | Silver | DOWN | 13.9 min | 29¢ | 37% | 6¢ | Open | — |
| 9/28 9:02:38 PM | Silver | DOWN | 12.4 min | 34¢ | 41% | 5¢ | ✅ Won | $6.44 |
| 9/28 9:01:26 PM | Gold | DOWN | 13.6 min | 42¢ | 49% | 5¢ | ✅ Won | $5.62 |
| 9/28 8:46:49 PM | Gold | UP | 13.2 min | 50¢ | 56% | 4¢ | ✅ Won | $4.82 |
| 9/28 8:46:37 PM | Silver | DOWN | 13.4 min | 30¢ | 38% | 7¢ | ✅ Won | $6.85 |
| 9/28 8:39:44 PM | Silver | UP | 5.3 min | 9¢ | 16% | 6¢ | ❌ Lost | -$0.95 |
| 9/28 8:31:02 PM | Gold | UP | 14.0 min | 53¢ | 61% | 6¢ | ✅ Won | $4.52 |
| 9/28 8:18:20 PM | Silver | DOWN | 11.7 min | 39¢ | 48% | 7¢ | ❌ Lost | -$4.07 |
| 9/28 8:17:38 PM | Gold | UP | 12.4 min | 45¢ | 51% | 5¢ | ✅ Won | $5.32 |
| 9/28 8:01:29 PM | Gold | UP | 13.5 min | 32¢ | 43% | 10¢ | ❌ Lost | -$3.36 |
| 9/28 8:01:07 PM | Silver | UP | 13.9 min | 42¢ | 48% | 4¢ | ❌ Lost | -$4.38 |
