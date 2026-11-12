# Range-Scalp Bot

*Updated Thu Nov 12 14:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57019 | 49700 | 7319 (101) | 0 | $-15719.47 | -4.4% |
| **+10¢** | 42617 | 34079 | 8538 (133) | 0 | $-14655.20 | -5.5% |
| **+15¢** | 35729 | 26541 | 9188 (167) | 0 | $-13251.93 | -5.9% |
| **+20¢** | 31833 | 22194 | 9639 (217) | 0 | $-11617.22 | -5.8% |
| **+10¢ (15¢ stop)** | 69531 | 69403 | 128 (78) | 0 | $-25689.30 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 14:19 | +10 stop | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-12 14:19 | +10 | BTC | DOWN | 0.70 | 0.80 | 0.73 |
| 11-12 14:19 | +5 | BTC | DOWN | 0.70 | 0.79 | 0.63 |
| 11-12 14:17 | +10 stop | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-12 14:17 | +10 | NEAR | DOWN | 0.71 | 0.81 | 0.74 |
| 11-12 14:17 | +5 | NEAR | DOWN | 0.67 | 0.72 | 0.19 |
| 11-12 14:17 | +10 stop | HYPE | DOWN | 0.61 | 0.73 | 0.89 |
| 11-12 14:17 | +20 | HYPE | DOWN | 0.61 | 0.85 | 2.14 |
| 11-12 14:17 | +15 | HYPE | DOWN | 0.62 | 0.78 | 1.30 |
| 11-12 14:17 | +10 | HYPE | DOWN | 0.63 | 0.73 | 0.73 |
| 11-12 14:17 | +5 | HYPE | DOWN | 0.63 | 0.69 | 0.32 |
| 11-12 14:17 | +10 stop | BTC | DOWN | 0.61 | 0.72 | 0.78 |
| 11-12 14:17 | +20 | BTC | DOWN | 0.62 | 0.86 | 2.14 |
| 11-12 14:17 | +15 | BTC | DOWN | 0.62 | 0.79 | 1.41 |
| 11-12 14:17 | +10 | BTC | DOWN | 0.62 | 0.72 | 0.68 |
| 11-12 14:17 | +5 | BTC | DOWN | 0.63 | 0.69 | 0.28 |
| 11-12 14:16 | +10 stop | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 11-12 14:16 | +20 | ETH | DOWN | 0.70 | 0.94 | 2.16 |
| 11-12 14:16 | +15 | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 11-12 14:16 | +10 | ETH | DOWN | 0.70 | 0.86 | 1.36 |
| 11-12 14:16 | +5 | ETH | DOWN | 0.70 | 0.75 | 0.21 |
| 11-12 14:16 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 11-12 14:16 | +20 | BNB | DOWN | 0.63 | 0.85 | 1.94 |
| 11-12 14:16 | +15 | BNB | DOWN | 0.64 | 0.82 | 1.52 |
| 11-12 14:16 | +10 | BNB | DOWN | 0.64 | 0.74 | 0.69 |
| 11-12 14:16 | +5 | BNB | DOWN | 0.63 | 0.71 | 0.48 |
| 11-12 14:16 | +10 stop | SOL | DOWN | 0.66 | 0.76 | 0.71 |
| 11-12 14:16 | +20 | SOL | DOWN | 0.64 | 0.86 | 1.94 |
| 11-12 14:16 | +15 | SOL | DOWN | 0.64 | 0.86 | 1.97 |
| 11-12 14:16 | +10 | SOL | DOWN | 0.62 | 0.74 | 0.89 |
| 11-12 14:16 | +5 | SOL | DOWN | 0.62 | 0.68 | 0.27 |
| 11-12 14:16 | +10 stop | NEAR | DOWN | 0.55 | 0.69 | 1.07 |
| 11-12 14:16 | +20 | NEAR | DOWN | 0.55 | 0.75 | 1.68 |
| 11-12 14:16 | +15 | NEAR | DOWN | 0.56 | 0.72 | 1.27 |
| 11-12 14:16 | +10 | NEAR | DOWN | 0.56 | 0.69 | 0.97 |
| 11-12 14:16 | +5 | NEAR | DOWN | 0.56 | 0.69 | 0.97 |
| 11-12 14:16 | +10 stop | XRP | DOWN | 0.70 | 0.80 | 0.73 |
| 11-12 14:16 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.88 |
| 11-12 14:16 | +15 | XRP | DOWN | 0.70 | 0.88 | 1.57 |
| 11-12 14:16 | +10 | XRP | DOWN | 0.70 | 0.80 | 0.73 |
