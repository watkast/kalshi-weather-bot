# Range-Scalp Bot

*Updated Mon Oct 19 00:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23180 | 20153 | 3027 (30) | 2 | $-6918.90 | -4.7% |
| **+10¢** | 17431 | 13938 | 3493 (44) | 3 | $-6211.14 | -5.7% |
| **+15¢** | 14613 | 10848 | 3765 (66) | 3 | $-5650.54 | -6.2% |
| **+20¢** | 12936 | 8999 | 3937 (84) | 3 | $-5032.95 | -6.2% |
| **+10¢ (15¢ stop)** | 28516 | 28465 | 51 (30) | 3 | $-10869.98 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 00:15 | +10 stop | XRP | DOWN | 0.66 | open |  |
| 10-19 00:15 | +20 | XRP | DOWN | 0.66 | open |  |
| 10-19 00:15 | +15 | XRP | DOWN | 0.66 | open |  |
| 10-19 00:15 | +10 | XRP | DOWN | 0.66 | open |  |
| 10-19 00:15 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.29 |
| 10-19 00:15 | +10 stop | ETH | DOWN | 0.65 | open |  |
| 10-19 00:15 | +20 | ETH | DOWN | 0.65 | open |  |
| 10-19 00:15 | +15 | ETH | DOWN | 0.65 | open |  |
| 10-19 00:15 | +10 | ETH | DOWN | 0.65 | open |  |
| 10-19 00:15 | +5 | ETH | DOWN | 0.65 | open |  |
| 10-19 00:15 | +10 stop | NEAR | DOWN | 0.66 | open |  |
| 10-19 00:15 | +20 | NEAR | DOWN | 0.66 | open |  |
| 10-19 00:15 | +15 | NEAR | DOWN | 0.65 | open |  |
| 10-19 00:15 | +10 | NEAR | DOWN | 0.65 | open |  |
| 10-19 00:15 | +5 | NEAR | DOWN | 0.65 | open |  |
| 10-19 00:14 | +10 stop | BNB | UP | 0.71 | 0.00 | -7.22 |
| 10-19 00:12 | +10 stop | DOGE | UP | 0.65 | 0.80 | 1.22 |
| 10-19 00:12 | +10 stop | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 10-19 00:12 | +15 | NEAR | UP | 0.70 | 0.91 | 1.89 |
| 10-19 00:12 | +10 | NEAR | UP | 0.70 | 0.81 | 0.84 |
| 10-19 00:12 | +5 | NEAR | UP | 0.70 | 0.76 | 0.32 |
| 10-19 00:11 | +10 stop | BTC | UP | 0.66 | 0.76 | 0.71 |
| 10-19 00:11 | +10 stop | SOL | UP | 0.60 | 0.70 | 0.68 |
| 10-19 00:11 | +10 | SOL | UP | 0.60 | 0.70 | 0.68 |
| 10-19 00:11 | +5 | SOL | UP | 0.60 | 0.70 | 0.68 |
| 10-19 00:11 | +10 stop | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 10-19 00:11 | +20 | NEAR | UP | 0.58 | 0.81 | 2.01 |
| 10-19 00:11 | +15 | NEAR | UP | 0.59 | 0.77 | 1.50 |
| 10-19 00:11 | +10 | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 10-19 00:11 | +5 | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 10-19 00:09 | +5 | SOL | UP | 0.71 | 0.76 | 0.22 |
| 10-19 00:08 | +5 | DOGE | DOWN | 0.67 | 0.85 | 1.55 |
| 10-19 00:08 | +10 stop | SOL | UP | 0.61 | 0.76 | 1.20 |
| 10-19 00:08 | +10 | SOL | UP | 0.61 | 0.76 | 1.20 |
| 10-19 00:08 | +5 | SOL | UP | 0.61 | 0.66 | 0.17 |
| 10-19 00:07 | +10 stop | ETH | UP | 0.68 | 0.78 | 0.71 |
| 10-19 00:07 | +10 stop | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 10-19 00:07 | +10 | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 10-19 00:07 | +5 | NEAR | UP | 0.65 | 0.77 | 0.91 |
| 10-19 00:07 | +10 stop | BTC | UP | 0.66 | 0.76 | 0.71 |
