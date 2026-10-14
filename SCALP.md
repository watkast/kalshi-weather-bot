# Range-Scalp Bot

*Updated Wed Oct 14 15:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16146 | 13987 | 2159 (27) | 0 | $-5112.01 | -5.0% |
| **+10¢** | 12203 | 9703 | 2500 (39) | 0 | $-4708.85 | -6.1% |
| **+15¢** | 10261 | 7575 | 2686 (58) | 1 | $-4225.03 | -6.6% |
| **+20¢** | 9129 | 6312 | 2817 (75) | 1 | $-3735.73 | -6.5% |
| **+10¢ (15¢ stop)** | 19879 | 19829 | 50 (29) | 0 | $-7635.54 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 15:24 | +10 stop | BTC | UP | 0.66 | 0.76 | 0.71 |
| 10-14 15:22 | +10 stop | BTC | UP | 0.61 | 0.46 | -1.85 |
| 10-14 15:22 | +20 | BTC | UP | 0.62 | open |  |
| 10-14 15:22 | +15 | BTC | UP | 0.62 | open |  |
| 10-14 15:22 | +10 | BTC | UP | 0.62 | 0.75 | 0.99 |
| 10-14 15:22 | +5 | BTC | UP | 0.62 | 0.69 | 0.38 |
| 10-14 15:22 | +5 | NEAR | UP | 0.66 | 0.71 | 0.19 |
| 10-14 15:22 | +10 stop | NEAR | UP | 0.62 | 0.75 | 0.99 |
| 10-14 15:22 | +20 | NEAR | UP | 0.62 | 0.85 | 2.04 |
| 10-14 15:22 | +15 | NEAR | UP | 0.62 | 0.85 | 2.04 |
| 10-14 15:22 | +10 | NEAR | UP | 0.62 | 0.75 | 0.99 |
| 10-14 15:22 | +5 | NEAR | UP | 0.62 | 0.67 | 0.17 |
| 10-14 15:07 | +10 stop | XRP | DOWN | 0.70 | 0.88 | 1.57 |
| 10-14 15:06 | +5 | BTC | DOWN | 0.66 | 0.72 | 0.29 |
| 10-14 15:05 | +5 | BTC | DOWN | 0.62 | 0.69 | 0.38 |
| 10-14 15:05 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 10-14 15:05 | +5 | DOGE | DOWN | 0.62 | 0.70 | 0.48 |
| 10-14 15:05 | +5 | SOL | DOWN | 0.68 | 0.77 | 0.61 |
| 10-14 15:04 | +10 stop | XRP | UP | 0.50 | 0.34 | -1.94 |
| 10-14 15:04 | +10 stop | ETH | UP | 0.61 | 0.37 | -2.74 |
| 10-14 15:04 | +10 stop | ZEC | DOWN | 0.70 | 0.80 | 0.73 |
| 10-14 15:04 | +15 | ZEC | DOWN | 0.70 | 0.86 | 1.33 |
| 10-14 15:04 | +10 | ZEC | DOWN | 0.70 | 0.84 | 1.12 |
| 10-14 15:04 | +5 | ZEC | DOWN | 0.70 | 0.80 | 0.71 |
| 10-14 15:04 | +5 | BTC | DOWN | 0.62 | 0.69 | 0.38 |
| 10-14 15:04 | +10 stop | SOL | DOWN | 0.59 | 0.77 | 1.50 |
| 10-14 15:04 | +10 | SOL | DOWN | 0.58 | 0.68 | 0.66 |
| 10-14 15:04 | +5 | SOL | DOWN | 0.58 | 0.63 | 0.15 |
| 10-14 15:04 | +5 | DOGE | DOWN | 0.58 | 0.66 | 0.46 |
| 10-14 15:04 | +10 stop | HYPE | DOWN | 0.55 | 0.70 | 1.17 |
| 10-14 15:02 | +10 stop | XRP | DOWN | 0.58 | 0.43 | -1.86 |
| 10-14 15:02 | +10 stop | NEAR | DOWN | 0.66 | 0.78 | 0.91 |
| 10-14 15:02 | +10 stop | BNB | DOWN | 0.59 | 0.69 | 0.68 |
| 10-14 15:01 | +10 stop | HYPE | DOWN | 0.68 | 0.52 | -1.94 |
| 10-14 15:01 | +20 | HYPE | DOWN | 0.68 | 0.88 | 1.76 |
| 10-14 15:01 | +15 | HYPE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-14 15:01 | +10 | HYPE | DOWN | 0.68 | 0.83 | 1.24 |
| 10-14 15:01 | +5 | HYPE | DOWN | 0.68 | 0.73 | 0.20 |
| 10-14 15:01 | +10 stop | ETH | DOWN | 0.63 | 0.48 | -1.85 |
| 10-14 15:01 | +20 | ETH | DOWN | 0.63 | 0.89 | 2.36 |
