# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 3:32 PM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 127 | 125 | 44 (35%) | 38¢ | 47% | -$60.71 | -12% |
| Silver | 64 | 63 | 20 (32%) | 33¢ | 41% | -$17.85 | -8% |
| Gold | 63 | 62 | 24 (39%) | 44¢ | 52% | -$42.86 | -15% |

*Earlier half -$29.50 / later half -$31.21.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 128 | 44 (34%) | -$90.95 | -17% |
| 4¢+ ← live bot | 125 | 46 (37%) | -$7.66 | -2% |
| 6¢+ | 113 | 49 (43%) | $99.45 | +25% |
| 8¢+ | 100 | 42 (42%) | $104.57 | +33% |
| 10¢+ | 87 | 33 (38%) | $68.12 | +26% |
| 15¢+ | 54 | 20 (37%) | $59.59 | +42% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 3196 | -1.8% |
| Hyperliquid price vs Kalshi's target | 3196 | +2.5% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 3:31:30 PM | Gold | UP | 13.5 min | 49¢ | 56% | 5¢ | Open | — |
| 9/29 3:31:18 PM | Silver | DOWN | 13.7 min | 27¢ | 35% | 7¢ | Open | — |
| 9/29 3:23:32 PM | Silver | UP | 6.5 min | 22¢ | 37% | 14¢ | ❌ Lost | -$2.33 |
| 9/29 3:16:35 PM | Gold | DOWN | 13.4 min | 47¢ | 53% | 4¢ | ✅ Won | $5.12 |
| 9/29 3:02:32 PM | Gold | DOWN | 12.5 min | 41¢ | 52% | 9¢ | ✅ Won | $5.73 |
| 9/29 3:01:02 PM | Silver | DOWN | 13.9 min | 14¢ | 49% | 34¢ | ❌ Lost | -$1.49 |
| 9/29 2:46:28 PM | Silver | UP | 13.5 min | 30¢ | 37% | 5¢ | ❌ Lost | -$3.15 |
| 9/29 2:46:03 PM | Gold | UP | 13.9 min | 32¢ | 52% | 18¢ | ❌ Lost | -$3.36 |
| 9/29 2:32:20 PM | Silver | DOWN | 12.7 min | 28¢ | 35% | 5¢ | ❌ Lost | -$2.95 |
| 9/29 2:31:04 PM | Gold | UP | 13.9 min | 41¢ | 50% | 7¢ | ✅ Won | $5.73 |
| 9/29 2:17:22 PM | Gold | DOWN | 12.6 min | 50¢ | 56% | 5¢ | ❌ Lost | -$5.18 |
| 9/29 2:16:04 PM | Silver | UP | 13.9 min | 30¢ | 38% | 7¢ | ✅ Won | $6.85 |
