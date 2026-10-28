# Range-Scalp Bot

*Updated Wed Oct 28 20:25 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38478 | 33578 | 4900 (48) | 0 | $-10802.61 | -4.5% |
| **+10¢** | 28699 | 23041 | 5658 (70) | 0 | $-9571.19 | -5.3% |
| **+15¢** | 24008 | 17932 | 6076 (95) | 0 | $-8508.48 | -5.6% |
| **+20¢** | 21298 | 14936 | 6362 (120) | 0 | $-7436.66 | -5.6% |
| **+10¢ (15¢ stop)** | 47067 | 47000 | 67 (35) | 0 | $-17866.09 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 20:21 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-28 20:21 | +20 | BTC | DOWN | 0.66 | 0.86 | 1.75 |
| 10-28 20:21 | +15 | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 10-28 20:21 | +10 | BTC | DOWN | 0.66 | 0.77 | 0.81 |
| 10-28 20:21 | +5 | BTC | DOWN | 0.66 | 0.71 | 0.19 |
| 10-28 20:18 | +10 stop | BNB | DOWN | 0.66 | 0.79 | 1.02 |
| 10-28 20:18 | +10 | BNB | DOWN | 0.66 | 0.79 | 1.02 |
| 10-28 20:18 | +5 | BNB | DOWN | 0.68 | 0.79 | 0.82 |
| 10-28 20:16 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-28 20:16 | +10 | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 10-28 20:16 | +10 stop | XRP | DOWN | 0.64 | 0.80 | 1.31 |
| 10-28 20:16 | +20 | XRP | DOWN | 0.64 | 0.85 | 1.84 |
| 10-28 20:16 | +15 | XRP | DOWN | 0.64 | 0.80 | 1.31 |
| 10-28 20:16 | +10 | XRP | DOWN | 0.64 | 0.80 | 1.31 |
| 10-28 20:16 | +5 | XRP | DOWN | 0.65 | 0.80 | 1.22 |
| 10-28 20:16 | +10 stop | BTC | DOWN | 0.61 | 0.72 | 0.78 |
| 10-28 20:16 | +20 | BTC | DOWN | 0.61 | 0.84 | 2.03 |
| 10-28 20:16 | +15 | BTC | DOWN | 0.61 | 0.78 | 1.40 |
| 10-28 20:16 | +10 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-28 20:16 | +5 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 10-28 20:16 | +10 stop | BNB | DOWN | 0.56 | 0.69 | 0.97 |
| 10-28 20:16 | +20 | BNB | DOWN | 0.56 | 0.79 | 2.00 |
| 10-28 20:16 | +15 | BNB | DOWN | 0.56 | 0.79 | 2.00 |
| 10-28 20:16 | +10 | BNB | DOWN | 0.56 | 0.69 | 0.97 |
| 10-28 20:16 | +5 | BNB | DOWN | 0.56 | 0.63 | 0.35 |
| 10-28 20:16 | +10 stop | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-28 20:16 | +20 | SOL | DOWN | 0.62 | 0.82 | 1.72 |
| 10-28 20:16 | +15 | SOL | DOWN | 0.62 | 0.80 | 1.51 |
| 10-28 20:16 | +10 | SOL | DOWN | 0.62 | 0.72 | 0.68 |
| 10-28 20:16 | +5 | SOL | DOWN | 0.62 | 0.71 | 0.58 |
| 10-28 20:16 | +10 stop | ETH | DOWN | 0.64 | 0.74 | 0.69 |
| 10-28 20:16 | +20 | ETH | DOWN | 0.64 | 0.85 | 1.84 |
| 10-28 20:16 | +15 | ETH | DOWN | 0.62 | 0.81 | 1.62 |
| 10-28 20:16 | +10 | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 10-28 20:16 | +5 | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 10-28 20:16 | +5 | DOGE | DOWN | 0.66 | 0.72 | 0.29 |
| 10-28 20:16 | +10 stop | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 10-28 20:16 | +20 | NEAR | DOWN | 0.60 | 0.80 | 1.71 |
| 10-28 20:16 | +15 | NEAR | DOWN | 0.60 | 0.77 | 1.40 |
| 10-28 20:16 | +10 | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
