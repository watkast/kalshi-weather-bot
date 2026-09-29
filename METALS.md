# Gold & Silver Fair-Value Bot

*Updated Mon Sep 28, 9:40 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

⏳ **Too early.** 18 of 30 settled trades needed before judging.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 20 | 18 | 9 (50%) | 36¢ | 44% | $21.52 | +31% |
| Silver | 10 | 9 | 3 (33%) | 31¢ | 38% | $1.18 | +4% |
| Gold | 10 | 9 | 6 (67%) | 42¢ | 50% | $20.34 | +51% |

*Earlier half $5.00 / later half $16.52.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 18 | 8 (44%) | $0.40 | +1% |
| 4¢+ ← live bot | 18 | 8 (44%) | $13.57 | +20% |
| 6¢+ | 18 | 7 (39%) | $15.55 | +29% |
| 8¢+ | 17 | 7 (41%) | $26.23 | +60% |
| 10¢+ | 15 | 4 (27%) | $9.23 | +30% |
| 15¢+ | 7 | 3 (43%) | $17.04 | +131% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 447 | -0.1% |
| Hyperliquid price vs Kalshi's target | 447 | +3.4% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/28 9:32:24 PM | Silver | DOWN | 12.6 min | 42¢ | 48% | 4¢ | Open | — |
| 9/28 9:32:08 PM | Gold | UP | 12.8 min | 42¢ | 52% | 8¢ | Open | — |
| 9/28 9:18:13 PM | Gold | DOWN | 11.8 min | 35¢ | 42% | 6¢ | ❌ Lost | -$3.66 |
| 9/28 9:16:07 PM | Silver | DOWN | 13.9 min | 29¢ | 37% | 6¢ | ❌ Lost | -$3.05 |
| 9/28 9:02:38 PM | Silver | DOWN | 12.4 min | 34¢ | 41% | 5¢ | ✅ Won | $6.44 |
| 9/28 9:01:26 PM | Gold | DOWN | 13.6 min | 42¢ | 49% | 5¢ | ✅ Won | $5.62 |
| 9/28 8:46:49 PM | Gold | UP | 13.2 min | 50¢ | 56% | 4¢ | ✅ Won | $4.82 |
| 9/28 8:46:37 PM | Silver | DOWN | 13.4 min | 30¢ | 38% | 7¢ | ✅ Won | $6.85 |
| 9/28 8:39:44 PM | Silver | UP | 5.3 min | 9¢ | 16% | 6¢ | ❌ Lost | -$0.95 |
| 9/28 8:31:02 PM | Gold | UP | 14.0 min | 53¢ | 61% | 6¢ | ✅ Won | $4.52 |
| 9/28 8:18:20 PM | Silver | DOWN | 11.7 min | 39¢ | 48% | 7¢ | ❌ Lost | -$4.07 |
| 9/28 8:17:38 PM | Gold | UP | 12.4 min | 45¢ | 51% | 5¢ | ✅ Won | $5.32 |
