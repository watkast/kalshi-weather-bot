# Range-Scalp Bot

*Updated Tue Nov 24 20:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71054 | 62021 | 9033 (155) | 1 | $-18931.68 | -4.2% |
| **+10¢** | 53003 | 42451 | 10552 (201) | 1 | $-17544.39 | -5.3% |
| **+15¢** | 44389 | 33028 | 11361 (258) | 1 | $-15596.60 | -5.6% |
| **+20¢** | 39517 | 27555 | 11962 (324) | 1 | $-13986.98 | -5.6% |
| **+10¢ (15¢ stop)** | 86497 | 86296 | 201 (121) | 0 | $-31793.33 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 20:24 | +5 | BTC | DOWN | 0.69 | 0.75 | 0.31 |
| 11-24 20:24 | +10 stop | SOL | DOWN | 0.67 | 0.81 | 1.13 |
| 11-24 20:23 | +10 stop | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 11-24 20:23 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-24 20:23 | +5 | ETH | DOWN | 0.70 | 0.75 | 0.21 |
| 11-24 20:23 | +10 stop | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-24 20:23 | +10 stop | SOL | DOWN | 0.67 | 0.52 | -1.84 |
| 11-24 20:21 | +10 stop | HYPE | UP | 0.50 | 0.67 | 1.36 |
| 11-24 20:21 | +10 stop | BNB | DOWN | 0.59 | 0.70 | 0.78 |
| 11-24 20:21 | +20 | BNB | DOWN | 0.59 | 0.79 | 1.71 |
| 11-24 20:21 | +15 | BNB | DOWN | 0.59 | 0.79 | 1.71 |
| 11-24 20:21 | +10 | BNB | DOWN | 0.59 | 0.70 | 0.78 |
| 11-24 20:21 | +5 | BNB | DOWN | 0.61 | 0.70 | 0.62 |
| 11-24 20:21 | +10 stop | DOGE | DOWN | 0.68 | 0.83 | 1.24 |
| 11-24 20:21 | +20 | DOGE | DOWN | 0.68 | 0.90 | 1.98 |
| 11-24 20:21 | +10 | DOGE | DOWN | 0.68 | 0.83 | 1.24 |
| 11-24 20:21 | +10 stop | SOL | UP | 0.63 | 0.48 | -1.85 |
| 11-24 20:21 | +10 | ETH | DOWN | 0.51 | 0.65 | 1.06 |
| 11-24 20:21 | +5 | ETH | DOWN | 0.52 | 0.65 | 0.96 |
| 11-24 20:21 | +5 | HYPE | UP | 0.65 | open |  |
| 11-24 20:20 | +5 | DOGE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-24 20:20 | +10 stop | NEAR | DOWN | 0.71 | 0.87 | 1.37 |
| 11-24 20:20 | +20 | NEAR | DOWN | 0.71 | 0.92 | 1.86 |
| 11-24 20:20 | +15 | NEAR | DOWN | 0.71 | 0.87 | 1.37 |
| 11-24 20:20 | +10 | NEAR | DOWN | 0.71 | 0.87 | 1.37 |
| 11-24 20:20 | +5 | NEAR | DOWN | 0.71 | 0.77 | 0.32 |
| 11-24 20:20 | +15 | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 11-24 20:20 | +15 | ETH | DOWN | 0.62 | 0.78 | 1.30 |
| 11-24 20:20 | +5 | ETH | DOWN | 0.63 | 0.72 | 0.58 |
| 11-24 20:20 | +10 stop | HYPE | DOWN | 0.51 | 0.34 | -2.04 |
| 11-24 20:20 | +10 | HYPE | DOWN | 0.52 | 0.63 | 0.75 |
| 11-24 20:20 | +5 | HYPE | DOWN | 0.52 | 0.58 | 0.24 |
| 11-24 20:19 | +10 stop | SOL | DOWN | 0.70 | 0.52 | -2.08 |
| 11-24 20:19 | +10 stop | ZEC | DOWN | 0.65 | 0.42 | -2.64 |
| 11-24 20:19 | +20 | ZEC | DOWN | 0.65 | 0.88 | 2.06 |
| 11-24 20:19 | +15 | ZEC | DOWN | 0.65 | 0.84 | 1.64 |
| 11-24 20:19 | +10 | ZEC | DOWN | 0.66 | 0.78 | 0.91 |
| 11-24 20:19 | +5 | ZEC | DOWN | 0.66 | 0.71 | 0.19 |
| 11-24 20:19 | +5 | SOL | DOWN | 0.68 | 0.73 | 0.20 |
| 11-24 20:19 | +10 stop | ETH | DOWN | 0.66 | 0.45 | -2.44 |
