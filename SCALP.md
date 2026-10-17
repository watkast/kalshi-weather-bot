# Range-Scalp Bot

*Updated Sat Oct 17 21:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 21601 | 18831 | 2770 (29) | 1 | $-6105.70 | -4.5% |
| **+10¢** | 16244 | 13039 | 3205 (41) | 1 | $-5435.41 | -5.3% |
| **+15¢** | 13583 | 10124 | 3459 (61) | 1 | $-4940.98 | -5.8% |
| **+20¢** | 12029 | 8404 | 3625 (80) | 1 | $-4392.72 | -5.8% |
| **+10¢ (15¢ stop)** | 26517 | 26467 | 50 (29) | 1 | $-10081.03 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-17 21:16 | +10 stop | ETH | DOWN | 0.69 | open |  |
| 10-17 21:16 | +20 | ETH | DOWN | 0.69 | open |  |
| 10-17 21:16 | +15 | ETH | DOWN | 0.69 | open |  |
| 10-17 21:16 | +10 | ETH | DOWN | 0.68 | open |  |
| 10-17 21:16 | +5 | ETH | DOWN | 0.68 | open |  |
| 10-17 21:11 | +10 stop | BTC | DOWN | 0.67 | 0.48 | -2.24 |
| 10-17 21:11 | +20 | BTC | DOWN | 0.67 | yes | -6.86 |
| 10-17 21:11 | +15 | BTC | DOWN | 0.67 | yes | -6.86 |
| 10-17 21:11 | +10 stop | ETH | DOWN | 0.58 | 0.32 | -2.94 |
| 10-17 21:10 | +10 stop | XRP | UP | 0.67 | 0.84 | 1.44 |
| 10-17 21:10 | +20 | XRP | UP | 0.67 | 0.93 | 2.43 |
| 10-17 21:10 | +15 | XRP | UP | 0.67 | 0.84 | 1.44 |
| 10-17 21:10 | +10 | XRP | UP | 0.68 | 0.84 | 1.34 |
| 10-17 21:10 | +5 | XRP | UP | 0.68 | 0.73 | 0.20 |
| 10-17 21:10 | +10 | BNB | DOWN | 0.45 | 0.59 | 1.05 |
| 10-17 21:10 | +5 | BNB | DOWN | 0.41 | 0.59 | 1.46 |
| 10-17 21:09 | +10 stop | BTC | DOWN | 0.55 | 0.66 | 0.76 |
| 10-17 21:09 | +10 stop | BNB | DOWN | 0.67 | 0.48 | -2.24 |
| 10-17 21:09 | +5 | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 10-17 21:08 | +10 stop | ETH | UP | 0.61 | 0.45 | -1.95 |
| 10-17 21:08 | +20 | ETH | UP | 0.61 | 0.82 | 1.82 |
| 10-17 21:08 | +15 | ETH | UP | 0.62 | 0.82 | 1.72 |
| 10-17 21:08 | +10 | ETH | UP | 0.62 | 0.75 | 0.99 |
| 10-17 21:08 | +5 | ETH | UP | 0.62 | 0.70 | 0.48 |
| 10-17 21:08 | +10 stop | HYPE | UP | 0.50 | 0.63 | 0.95 |
| 10-17 21:08 | +20 | HYPE | UP | 0.50 | 0.97 | 4.48 |
| 10-17 21:08 | +15 | HYPE | UP | 0.50 | 0.97 | 4.48 |
| 10-17 21:08 | +10 | HYPE | UP | 0.50 | 0.63 | 0.95 |
| 10-17 21:08 | +5 | HYPE | UP | 0.50 | 0.63 | 0.95 |
| 10-17 21:08 | +10 stop | SOL | UP | 0.52 | 0.31 | -2.43 |
| 10-17 21:08 | +15 | SOL | UP | 0.52 | 0.78 | 2.29 |
| 10-17 21:08 | +10 | SOL | UP | 0.52 | 0.78 | 2.26 |
| 10-17 21:08 | +5 | SOL | UP | 0.50 | 0.56 | 0.24 |
| 10-17 21:07 | +10 stop | NEAR | UP | 0.66 | 0.45 | -2.44 |
| 10-17 21:07 | +10 stop | BNB | UP | 0.71 | 0.53 | -2.13 |
| 10-17 21:06 | +5 | BTC | UP | 0.71 | 0.84 | 1.05 |
| 10-17 21:06 | +10 stop | ZEC | UP | 0.66 | 0.50 | -1.94 |
| 10-17 21:06 | +20 | ZEC | UP | 0.66 | no | -6.76 |
| 10-17 21:06 | +15 | ZEC | UP | 0.66 | no | -6.76 |
| 10-17 21:06 | +10 | ZEC | UP | 0.66 | no | -6.76 |
