# Range-Scalp Bot

*Updated Mon Oct 26 16:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 35114 | 30657 | 4457 (43) | 0 | $-9742.75 | -4.4% |
| **+10¢** | 26278 | 21125 | 5153 (65) | 0 | $-8535.44 | -5.2% |
| **+15¢** | 21984 | 16436 | 5548 (89) | 0 | $-7645.23 | -5.5% |
| **+20¢** | 19489 | 13674 | 5815 (112) | 0 | $-6713.41 | -5.5% |
| **+10¢ (15¢ stop)** | 42986 | 42924 | 62 (33) | 0 | $-16269.25 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-26 16:34 | +10 stop | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-26 16:34 | +10 | XRP | DOWN | 0.64 | 0.74 | 0.69 |
| 10-26 16:34 | +5 | XRP | DOWN | 0.64 | 0.72 | 0.48 |
| 10-26 16:34 | +5 | ETH | DOWN | 0.65 | 0.70 | 0.19 |
| 10-26 16:34 | +10 stop | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-26 16:34 | +20 | DOGE | DOWN | 0.71 | 0.92 | 1.88 |
| 10-26 16:34 | +15 | DOGE | DOWN | 0.71 | 0.86 | 1.26 |
| 10-26 16:34 | +10 | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-26 16:34 | +5 | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 10-26 16:34 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-26 16:34 | +20 | HYPE | DOWN | 0.69 | 0.89 | 1.78 |
| 10-26 16:34 | +15 | HYPE | DOWN | 0.69 | 0.89 | 1.74 |
| 10-26 16:34 | +10 | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-26 16:34 | +5 | HYPE | DOWN | 0.70 | 0.78 | 0.52 |
| 10-26 16:33 | +10 stop | ETH | DOWN | 0.58 | 0.69 | 0.77 |
| 10-26 16:33 | +20 | ETH | DOWN | 0.57 | 0.77 | 1.69 |
| 10-26 16:33 | +15 | ETH | DOWN | 0.57 | 0.75 | 1.48 |
| 10-26 16:33 | +10 | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 10-26 16:33 | +5 | ETH | DOWN | 0.57 | 0.64 | 0.35 |
| 10-26 16:33 | +10 stop | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-26 16:33 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 10-26 16:33 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 10-26 16:33 | +10 stop | NEAR | DOWN | 0.57 | 0.73 | 1.28 |
| 10-26 16:33 | +15 | NEAR | DOWN | 0.57 | 0.73 | 1.28 |
| 10-26 16:33 | +10 | NEAR | DOWN | 0.57 | 0.73 | 1.28 |
| 10-26 16:33 | +5 | NEAR | DOWN | 0.57 | 0.64 | 0.35 |
| 10-26 16:31 | +10 stop | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-26 16:31 | +10 stop | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 10-26 16:31 | +20 | NEAR | DOWN | 0.69 | 0.96 | 2.51 |
| 10-26 16:31 | +15 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 10-26 16:31 | +10 | NEAR | DOWN | 0.69 | 0.85 | 1.36 |
| 10-26 16:31 | +5 | NEAR | DOWN | 0.69 | 0.75 | 0.31 |
| 10-26 16:31 | +10 stop | ETH | DOWN | 0.62 | 0.76 | 1.10 |
| 10-26 16:31 | +20 | ETH | DOWN | 0.62 | 0.82 | 1.72 |
| 10-26 16:31 | +15 | ETH | DOWN | 0.62 | 0.82 | 1.72 |
| 10-26 16:31 | +10 | ETH | DOWN | 0.62 | 0.76 | 1.10 |
| 10-26 16:31 | +5 | ETH | DOWN | 0.62 | 0.69 | 0.38 |
| 10-26 16:31 | +10 stop | BTC | DOWN | 0.69 | 0.81 | 0.94 |
| 10-26 16:31 | +20 | BTC | DOWN | 0.69 | 0.92 | 2.07 |
| 10-26 16:31 | +15 | BTC | DOWN | 0.69 | 0.84 | 1.25 |
