# Range-Scalp Bot

*Updated Fri Nov 06 20:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49902 | 43497 | 6405 (76) | 1 | $-14028.57 | -4.5% |
| **+10¢** | 37250 | 29798 | 7452 (102) | 1 | $-12922.41 | -5.5% |
| **+15¢** | 31200 | 23169 | 8031 (131) | 1 | $-11836.74 | -6.0% |
| **+20¢** | 27737 | 19317 | 8420 (172) | 1 | $-10474.95 | -6.0% |
| **+10¢ (15¢ stop)** | 60812 | 60713 | 99 (58) | 0 | $-22554.72 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 20:22 | +10 stop | ZEC | DOWN | 0.47 | 0.62 | 1.15 |
| 11-06 20:20 | +10 stop | ZEC | UP | 0.62 | 0.45 | -2.05 |
| 11-06 20:20 | +15 | ZEC | UP | 0.62 | open |  |
| 11-06 20:20 | +10 | ZEC | UP | 0.63 | open |  |
| 11-06 20:20 | +5 | ZEC | UP | 0.63 | open |  |
| 11-06 20:19 | +5 | NEAR | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 20:18 | +5 | HYPE | DOWN | 0.59 | 0.71 | 0.88 |
| 11-06 20:18 | +5 | ETH | DOWN | 0.67 | 0.83 | 1.34 |
| 11-06 20:17 | +10 stop | BNB | DOWN | 0.58 | 0.72 | 1.03 |
| 11-06 20:17 | +20 | BNB | DOWN | 0.58 | 0.81 | 1.97 |
| 11-06 20:17 | +15 | BNB | DOWN | 0.58 | 0.81 | 1.97 |
| 11-06 20:17 | +10 | BNB | DOWN | 0.58 | 0.72 | 1.03 |
| 11-06 20:17 | +5 | BNB | DOWN | 0.58 | 0.66 | 0.42 |
| 11-06 20:17 | +10 stop | NEAR | DOWN | 0.56 | 0.78 | 1.89 |
| 11-06 20:17 | +20 | NEAR | DOWN | 0.56 | 0.78 | 1.89 |
| 11-06 20:17 | +15 | NEAR | DOWN | 0.56 | 0.78 | 1.89 |
| 11-06 20:17 | +10 | NEAR | DOWN | 0.56 | 0.78 | 1.89 |
| 11-06 20:17 | +5 | NEAR | DOWN | 0.56 | 0.64 | 0.45 |
| 11-06 20:17 | +10 stop | XRP | DOWN | 0.64 | 0.80 | 1.31 |
| 11-06 20:17 | +10 | XRP | DOWN | 0.64 | 0.80 | 1.31 |
| 11-06 20:17 | +10 stop | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-06 20:17 | +20 | BTC | DOWN | 0.62 | 0.82 | 1.72 |
| 11-06 20:17 | +15 | BTC | DOWN | 0.62 | 0.82 | 1.72 |
| 11-06 20:17 | +10 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-06 20:17 | +5 | BTC | DOWN | 0.62 | 0.68 | 0.27 |
| 11-06 20:17 | +5 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 11-06 20:17 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 11-06 20:17 | +20 | SOL | DOWN | 0.62 | 0.85 | 2.04 |
| 11-06 20:17 | +15 | SOL | DOWN | 0.62 | 0.85 | 2.04 |
| 11-06 20:17 | +10 | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 11-06 20:17 | +5 | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 11-06 20:16 | +10 stop | HYPE | DOWN | 0.56 | 0.71 | 1.17 |
| 11-06 20:16 | +20 | HYPE | DOWN | 0.56 | 0.87 | 2.84 |
| 11-06 20:16 | +15 | HYPE | DOWN | 0.56 | 0.71 | 1.17 |
| 11-06 20:16 | +10 | HYPE | DOWN | 0.56 | 0.71 | 1.17 |
| 11-06 20:16 | +5 | HYPE | DOWN | 0.56 | 0.62 | 0.25 |
| 11-06 20:16 | +10 stop | ETH | DOWN | 0.60 | 0.71 | 0.78 |
| 11-06 20:16 | +20 | ETH | DOWN | 0.60 | 0.83 | 2.03 |
| 11-06 20:16 | +15 | ETH | DOWN | 0.60 | 0.83 | 2.03 |
| 11-06 20:16 | +10 | ETH | DOWN | 0.60 | 0.71 | 0.78 |
