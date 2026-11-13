# Range-Scalp Bot

*Updated Fri Nov 13 01:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57605 | 50236 | 7369 (101) | 0 | $-15727.54 | -4.3% |
| **+10¢** | 43058 | 34452 | 8606 (133) | 0 | $-14667.73 | -5.4% |
| **+15¢** | 36099 | 26837 | 9262 (167) | 0 | $-13222.91 | -5.8% |
| **+20¢** | 32161 | 22443 | 9718 (217) | 0 | $-11577.63 | -5.7% |
| **+10¢ (15¢ stop)** | 70229 | 70101 | 128 (78) | 0 | $-25847.92 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 01:36 | +10 stop | NEAR | DOWN | 0.59 | 0.72 | 0.98 |
| 11-13 01:36 | +15 | NEAR | DOWN | 0.59 | 0.75 | 1.29 |
| 11-13 01:36 | +10 | NEAR | DOWN | 0.59 | 0.72 | 0.98 |
| 11-13 01:36 | +5 | NEAR | DOWN | 0.59 | 0.68 | 0.57 |
| 11-13 01:35 | +10 stop | DOGE | DOWN | 0.61 | 0.75 | 1.05 |
| 11-13 01:35 | +10 | DOGE | DOWN | 0.61 | 0.75 | 1.09 |
| 11-13 01:35 | +10 stop | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 11-13 01:35 | +10 | SOL | DOWN | 0.67 | 0.82 | 1.23 |
| 11-13 01:35 | +5 | SOL | DOWN | 0.68 | 0.73 | 0.20 |
| 11-13 01:34 | +5 | DOGE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-13 01:33 | +5 | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-13 01:33 | +10 stop | XRP | DOWN | 0.61 | 0.73 | 0.89 |
| 11-13 01:33 | +5 | XRP | DOWN | 0.62 | 0.73 | 0.79 |
| 11-13 01:33 | +10 stop | NEAR | DOWN | 0.64 | 0.74 | 0.69 |
| 11-13 01:33 | +10 stop | DOGE | DOWN | 0.61 | 0.72 | 0.78 |
| 11-13 01:32 | +5 | HYPE | DOWN | 0.61 | 0.68 | 0.37 |
| 11-13 01:32 | +5 | ETH | DOWN | 0.54 | 0.65 | 0.76 |
| 11-13 01:32 | +10 stop | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-13 01:32 | +20 | ZEC | DOWN | 0.60 | 0.81 | 1.82 |
| 11-13 01:32 | +15 | ZEC | DOWN | 0.59 | 0.76 | 1.40 |
| 11-13 01:32 | +10 | ZEC | DOWN | 0.60 | 0.76 | 1.30 |
| 11-13 01:32 | +5 | ZEC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-13 01:31 | +10 stop | HYPE | DOWN | 0.61 | 0.72 | 0.78 |
| 11-13 01:31 | +5 | HYPE | DOWN | 0.60 | 0.67 | 0.34 |
| 11-13 01:31 | +10 stop | BNB | DOWN | 0.61 | 0.73 | 0.87 |
| 11-13 01:31 | +20 | BNB | DOWN | 0.61 | 0.83 | 1.91 |
| 11-13 01:31 | +15 | BNB | DOWN | 0.62 | 0.80 | 1.54 |
| 11-13 01:31 | +10 | BNB | DOWN | 0.62 | 0.73 | 0.82 |
| 11-13 01:31 | +5 | BNB | DOWN | 0.62 | 0.73 | 0.80 |
| 11-13 01:31 | +10 stop | ETH | DOWN | 0.58 | 0.73 | 1.18 |
| 11-13 01:31 | +20 | ETH | DOWN | 0.58 | 0.81 | 2.01 |
| 11-13 01:31 | +15 | ETH | DOWN | 0.57 | 0.73 | 1.28 |
| 11-13 01:31 | +10 | ETH | DOWN | 0.56 | 0.73 | 1.38 |
| 11-13 01:31 | +5 | ETH | DOWN | 0.56 | 0.63 | 0.35 |
| 11-13 01:31 | +10 stop | BTC | DOWN | 0.59 | 0.72 | 0.98 |
| 11-13 01:31 | +20 | BTC | DOWN | 0.59 | 0.81 | 1.92 |
| 11-13 01:31 | +15 | BTC | DOWN | 0.59 | 0.81 | 1.92 |
| 11-13 01:31 | +10 | BTC | DOWN | 0.59 | 0.72 | 0.98 |
| 11-13 01:31 | +5 | BTC | DOWN | 0.59 | 0.68 | 0.57 |
| 11-13 01:31 | +10 stop | NEAR | DOWN | 0.62 | 0.44 | -2.15 |
