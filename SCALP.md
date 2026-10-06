# Range-Scalp Bot

*Updated Tue Oct 06 04:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 4643 | 4011 | 632 (6) | 4 | $-1519.89 | -5.2% |
| **+10¢** | 3570 | 2835 | 735 (9) | 6 | $-1408.93 | -6.3% |
| **+15¢** | 2999 | 2223 | 776 (12) | 7 | $-1206.63 | -6.4% |
| **+20¢** | 2690 | 1881 | 809 (17) | 9 | $-995.00 | -5.9% |
| **+10¢ (15¢ stop)** | 5693 | 5682 | 11 (6) | 5 | $-2063.87 | -5.8% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 04:17 | +5 | NEAR | UP | 0.57 | open |  |
| 10-06 04:17 | +15 | DOGE | UP | 0.61 | open |  |
| 10-06 04:17 | +10 stop | DOGE | UP | 0.70 | open |  |
| 10-06 04:17 | +10 | DOGE | UP | 0.70 | open |  |
| 10-06 04:17 | +5 | DOGE | UP | 0.70 | open |  |
| 10-06 04:16 | +10 stop | HYPE | UP | 0.58 | open |  |
| 10-06 04:16 | +20 | HYPE | UP | 0.58 | open |  |
| 10-06 04:16 | +15 | HYPE | UP | 0.58 | open |  |
| 10-06 04:16 | +10 | HYPE | UP | 0.58 | open |  |
| 10-06 04:16 | +5 | HYPE | UP | 0.58 | open |  |
| 10-06 04:16 | +10 stop | BNB | DOWN | 0.53 | open |  |
| 10-06 04:16 | +20 | BNB | DOWN | 0.53 | open |  |
| 10-06 04:16 | +15 | BNB | DOWN | 0.53 | open |  |
| 10-06 04:16 | +10 | BNB | DOWN | 0.54 | open |  |
| 10-06 04:16 | +5 | BNB | DOWN | 0.54 | 0.62 | 0.45 |
| 10-06 04:16 | +10 stop | DOGE | UP | 0.50 | 0.60 | 0.65 |
| 10-06 04:16 | +20 | DOGE | UP | 0.50 | open |  |
| 10-06 04:16 | +15 | DOGE | UP | 0.50 | 0.65 | 1.16 |
| 10-06 04:16 | +10 | DOGE | UP | 0.50 | 0.60 | 0.65 |
| 10-06 04:16 | +5 | DOGE | UP | 0.50 | 0.60 | 0.65 |
| 10-06 04:16 | +10 stop | BTC | DOWN | 0.58 | 0.42 | -1.96 |
| 10-06 04:16 | +20 | BTC | DOWN | 0.58 | open |  |
| 10-06 04:16 | +15 | BTC | DOWN | 0.58 | open |  |
| 10-06 04:16 | +10 | BTC | DOWN | 0.58 | open |  |
| 10-06 04:16 | +5 | BTC | DOWN | 0.58 | open |  |
| 10-06 04:16 | +10 stop | SOL | UP | 0.66 | open |  |
| 10-06 04:16 | +20 | SOL | UP | 0.65 | open |  |
| 10-06 04:16 | +15 | SOL | UP | 0.65 | open |  |
| 10-06 04:16 | +10 | SOL | UP | 0.65 | open |  |
| 10-06 04:16 | +5 | SOL | UP | 0.65 | 0.74 | 0.60 |
| 10-06 04:16 | +10 stop | NEAR | UP | 0.60 | open |  |
| 10-06 04:16 | +20 | NEAR | UP | 0.60 | open |  |
| 10-06 04:16 | +15 | NEAR | UP | 0.60 | open |  |
| 10-06 04:16 | +10 | NEAR | UP | 0.60 | open |  |
| 10-06 04:16 | +5 | NEAR | UP | 0.60 | 0.65 | 0.17 |
| 10-06 04:16 | +10 stop | ETH | UP | 0.57 | 0.70 | 0.97 |
| 10-06 04:16 | +20 | ETH | UP | 0.57 | open |  |
| 10-06 04:16 | +15 | ETH | UP | 0.57 | 0.74 | 1.38 |
| 10-06 04:16 | +10 | ETH | UP | 0.57 | 0.70 | 0.97 |
| 10-06 04:16 | +5 | ETH | UP | 0.57 | 0.64 | 0.35 |
