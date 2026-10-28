# Range-Scalp Bot

*Updated Wed Oct 28 14:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38221 | 33348 | 4873 (46) | 0 | $-10784.27 | -4.5% |
| **+10¢** | 28511 | 22880 | 5631 (68) | 0 | $-9585.40 | -5.3% |
| **+15¢** | 23856 | 17811 | 6045 (93) | 0 | $-8518.33 | -5.7% |
| **+20¢** | 21163 | 14832 | 6331 (118) | 0 | $-7479.26 | -5.6% |
| **+10¢ (15¢ stop)** | 46782 | 46715 | 67 (35) | 0 | $-17753.60 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 14:20 | +5 | NEAR | UP | 0.57 | no | -5.88 |
| 10-28 14:19 | +10 stop | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 10-28 14:19 | +15 | XRP | DOWN | 0.62 | 0.82 | 1.72 |
| 10-28 14:19 | +10 | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 10-28 14:19 | +5 | XRP | DOWN | 0.62 | 0.75 | 0.99 |
| 10-28 14:19 | +10 stop | ETH | DOWN | 0.64 | 0.80 | 1.31 |
| 10-28 14:19 | +20 | ETH | DOWN | 0.64 | 0.84 | 1.73 |
| 10-28 14:19 | +15 | ETH | DOWN | 0.64 | 0.80 | 1.31 |
| 10-28 14:19 | +10 | ETH | DOWN | 0.64 | 0.80 | 1.31 |
| 10-28 14:19 | +5 | ETH | DOWN | 0.64 | 0.70 | 0.28 |
| 10-28 14:19 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-28 14:19 | +20 | DOGE | DOWN | 0.68 | 0.90 | 1.99 |
| 10-28 14:19 | +15 | DOGE | DOWN | 0.68 | 0.85 | 1.45 |
| 10-28 14:19 | +10 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-28 14:19 | +5 | DOGE | DOWN | 0.68 | 0.76 | 0.51 |
| 10-28 14:19 | +10 stop | BNB | DOWN | 0.68 | 0.83 | 1.20 |
| 10-28 14:19 | +10 | BNB | DOWN | 0.68 | 0.83 | 1.20 |
| 10-28 14:19 | +5 | BNB | DOWN | 0.68 | 0.74 | 0.26 |
| 10-28 14:19 | +10 stop | SOL | DOWN | 0.67 | 0.84 | 1.44 |
| 10-28 14:19 | +20 | SOL | DOWN | 0.67 | 0.92 | 2.28 |
| 10-28 14:19 | +15 | SOL | DOWN | 0.67 | 0.84 | 1.44 |
| 10-28 14:19 | +10 | SOL | DOWN | 0.67 | 0.84 | 1.44 |
| 10-28 14:19 | +5 | SOL | DOWN | 0.68 | 0.74 | 0.30 |
| 10-28 14:19 | +10 stop | HYPE | DOWN | 0.60 | 0.71 | 0.78 |
| 10-28 14:19 | +10 | HYPE | DOWN | 0.60 | 0.71 | 0.78 |
| 10-28 14:19 | +10 stop | NEAR | DOWN | 0.52 | 0.71 | 1.57 |
| 10-28 14:19 | +20 | NEAR | DOWN | 0.52 | 0.75 | 1.98 |
| 10-28 14:19 | +15 | NEAR | DOWN | 0.52 | 0.71 | 1.57 |
| 10-28 14:19 | +10 | NEAR | DOWN | 0.52 | 0.71 | 1.57 |
| 10-28 14:19 | +5 | NEAR | DOWN | 0.52 | 0.58 | 0.24 |
| 10-28 14:17 | +5 | HYPE | DOWN | 0.68 | 0.80 | 0.92 |
| 10-28 14:16 | +10 stop | NEAR | DOWN | 0.57 | 0.70 | 0.97 |
| 10-28 14:16 | +20 | NEAR | DOWN | 0.56 | 0.76 | 1.69 |
| 10-28 14:16 | +15 | NEAR | DOWN | 0.56 | 0.73 | 1.38 |
| 10-28 14:16 | +10 | NEAR | DOWN | 0.55 | 0.65 | 0.66 |
| 10-28 14:16 | +5 | NEAR | DOWN | 0.55 | 0.65 | 0.66 |
| 10-28 14:16 | +10 stop | XRP | DOWN | 0.59 | 0.71 | 0.88 |
| 10-28 14:16 | +20 | XRP | DOWN | 0.59 | 0.82 | 2.02 |
| 10-28 14:16 | +15 | XRP | DOWN | 0.59 | 0.75 | 1.29 |
| 10-28 14:16 | +10 | XRP | DOWN | 0.59 | 0.71 | 0.88 |
