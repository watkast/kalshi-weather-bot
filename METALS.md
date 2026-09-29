# Gold & Silver Fair-Value Bot

*Updated Tue Sep 29, 11:10 AM MT. Paper money. Kalshi's 15-minute gold and silver up/down markets: every 2 seconds the bot works out the fair chance of UP from how far the metal has moved since the window started (live Hyperliquid prices), time left and recent volatility, then buys whichever side's real order-book price is at least 4¢ below fair value after fees (10 contracts, held to the close).*

[← Back to all bots](README.md) · [Crypto Fair-Value Bot](FAIRVALUE.md)

## Verdict

🔴 **Losing.** Not beating Kalshi's prices after fees.

## Live results

| | Trades | Settled | Won | Avg price paid | Model's avg chance | P&L | Return |
|---|---|---|---|---|---|---|---|
| **All** | 92 | 90 | 29 (32%) | 39¢ | 47% | -$75.91 | -21% |
| Silver | 47 | 46 | 14 (30%) | 34¢ | 41% | -$21.26 | -13% |
| Gold | 45 | 44 | 15 (34%) | 45¢ | 53% | -$54.65 | -27% |

*Earlier half -$32.92 / later half -$42.99.*

*If the model is right, the win rate should land near the model's average chance, above the average price paid.*

## Which edge threshold works best?

*Replayed from the 30-second shadow log (quoted prices, so a little optimistic).*

| Buy when edge is | Trades | Won | P&L | Return |
|---|---|---|---|---|
| 2¢+ | 93 | 29 (31%) | -$95.01 | -25% |
| 4¢+ ← live bot | 90 | 30 (33%) | -$32.11 | -10% |
| 6¢+ | 79 | 31 (39%) | $40.73 | +15% |
| 8¢+ | 66 | 28 (42%) | $66.00 | +31% |
| 10¢+ | 54 | 19 (35%) | $22.15 | +13% |
| 15¢+ | 29 | 10 (34%) | $23.08 | +30% |

## Does the model beat the market?

| Model | Readings scored | Accuracy vs Kalshi |
|---|---|---|
| Move since window start (live bot) | 2282 | -2.0% |
| Hyperliquid price vs Kalshi's target | 2282 | +1.1% |

*Log-loss skill, excluding the final minute. Positive = the model predicted outcomes better than Kalshi's price.*

## Latest trades

| When (MT) | Metal | Side | Time left | Paid | Model | Edge | Result | P&L |
|---|---|---|---|---|---|---|---|---|
| 9/29 11:01:35 AM | Silver | DOWN | 13.4 min | 36¢ | 44% | 6¢ | Open | — |
| 9/29 11:01:13 AM | Gold | DOWN | 13.8 min | 45¢ | 52% | 5¢ | Open | — |
| 9/29 10:50:18 AM | Silver | DOWN | 9.7 min | 29¢ | 36% | 6¢ | ✅ Won | $6.95 |
| 9/29 10:46:06 AM | Gold | UP | 13.9 min | 32¢ | 39% | 6¢ | ❌ Lost | -$3.36 |
| 9/29 10:38:20 AM | Gold | UP | 6.7 min | 48¢ | 55% | 5¢ | ❌ Lost | -$4.98 |
| 9/29 10:37:40 AM | Silver | DOWN | 7.3 min | 17¢ | 26% | 8¢ | ✅ Won | $8.20 |
| 9/29 8:18:54 AM | Silver | DOWN | 11.1 min | 38¢ | 44% | 4¢ | ❌ Lost | -$3.98 |
| 9/29 8:16:12 AM | Gold | DOWN | 13.8 min | 46¢ | 52% | 4¢ | ❌ Lost | -$4.78 |
| 9/29 8:01:24 AM | Gold | DOWN | 13.6 min | 19¢ | 25% | 5¢ | ❌ Lost | -$2.01 |
| 9/29 8:01:02 AM | Silver | DOWN | 13.9 min | 17¢ | 23% | 5¢ | ❌ Lost | -$1.80 |
| 9/29 7:46:04 AM | Silver | DOWN | 13.9 min | 37¢ | 43% | 4¢ | ❌ Lost | -$3.87 |
| 9/29 7:39:00 AM | Silver | UP | 6.0 min | 34¢ | 41% | 6¢ | ❌ Lost | -$3.56 |
