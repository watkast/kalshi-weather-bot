# Range-Scalp Bot

*Updated Thu Nov 12 13:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56976 | 49668 | 7308 (101) | 0 | $-15666.01 | -4.4% |
| **+10¢** | 42577 | 34050 | 8527 (133) | 0 | $-14612.48 | -5.5% |
| **+15¢** | 35698 | 26521 | 9177 (167) | 0 | $-13212.34 | -5.9% |
| **+20¢** | 31804 | 22176 | 9628 (217) | 0 | $-11585.10 | -5.8% |
| **+10¢ (15¢ stop)** | 69465 | 69337 | 128 (78) | 0 | $-25677.84 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 13:41 | +10 stop | XRP | UP | 0.54 | 0.82 | 2.51 |
| 11-12 13:41 | +10 | XRP | UP | 0.53 | 0.82 | 2.61 |
| 11-12 13:41 | +5 | XRP | UP | 0.52 | 0.62 | 0.65 |
| 11-12 13:41 | +10 stop | SOL | UP | 0.68 | 0.89 | 1.87 |
| 11-12 13:41 | +5 | SOL | UP | 0.68 | 0.89 | 1.87 |
| 11-12 13:40 | +10 stop | BTC | DOWN | 0.70 | 0.53 | -2.03 |
| 11-12 13:40 | +10 stop | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-12 13:40 | +5 | ZEC | UP | 0.68 | 0.93 | 2.24 |
| 11-12 13:40 | +10 stop | XRP | UP | 0.57 | 0.68 | 0.71 |
| 11-12 13:40 | +10 | XRP | UP | 0.57 | 0.68 | 0.71 |
| 11-12 13:40 | +5 | XRP | UP | 0.57 | 0.68 | 0.71 |
| 11-12 13:40 | +10 stop | ETH | UP | 0.63 | 0.84 | 1.83 |
| 11-12 13:40 | +10 stop | DOGE | UP | 0.41 | 0.55 | 1.06 |
| 11-12 13:39 | +10 stop | BNB | DOWN | 0.54 | 0.65 | 0.76 |
| 11-12 13:39 | +10 stop | ZEC | UP | 0.65 | 0.49 | -1.94 |
| 11-12 13:39 | +10 stop | HYPE | UP | 0.64 | 0.80 | 1.32 |
| 11-12 13:39 | +5 | HYPE | UP | 0.64 | 0.70 | 0.28 |
| 11-12 13:39 | +10 stop | SOL | UP | 0.64 | 0.78 | 1.10 |
| 11-12 13:39 | +5 | SOL | UP | 0.64 | 0.71 | 0.38 |
| 11-12 13:38 | +10 stop | NEAR | DOWN | 0.60 | 0.75 | 1.19 |
| 11-12 13:38 | +10 stop | DOGE | DOWN | 0.61 | 0.40 | -2.44 |
| 11-12 13:38 | +10 stop | BTC | DOWN | 0.60 | 0.72 | 0.88 |
| 11-12 13:38 | +10 stop | XRP | UP | 0.54 | 0.66 | 0.86 |
| 11-12 13:38 | +10 | XRP | UP | 0.55 | 0.66 | 0.76 |
| 11-12 13:38 | +5 | XRP | UP | 0.54 | 0.66 | 0.85 |
| 11-12 13:37 | +5 | BTC | UP | 0.67 | 0.86 | 1.65 |
| 11-12 13:37 | +10 stop | ZEC | UP | 0.66 | 0.47 | -2.24 |
| 11-12 13:37 | +10 stop | NEAR | UP | 0.60 | 0.35 | -2.86 |
| 11-12 13:36 | +10 stop | ETH | UP | 0.68 | 0.45 | -2.64 |
| 11-12 13:36 | +5 | ETH | UP | 0.70 | 0.84 | 1.15 |
| 11-12 13:36 | +10 stop | BNB | DOWN | 0.44 | 0.54 | 0.64 |
| 11-12 13:36 | +10 stop | NEAR | DOWN | 0.37 | 0.52 | 1.15 |
| 11-12 13:36 | +10 stop | HYPE | UP | 0.65 | 0.48 | -2.04 |
| 11-12 13:36 | +10 | HYPE | UP | 0.65 | 0.80 | 1.22 |
| 11-12 13:36 | +5 | HYPE | UP | 0.65 | 0.70 | 0.19 |
| 11-12 13:35 | +10 stop | ZEC | UP | 0.68 | 0.50 | -2.14 |
| 11-12 13:35 | +5 | NEAR | UP | 0.69 | 0.84 | 1.25 |
| 11-12 13:35 | +20 | NEAR | UP | 0.63 | 0.84 | 1.83 |
| 11-12 13:35 | +10 stop | ETH | UP | 0.65 | 0.49 | -1.94 |
| 11-12 13:35 | +10 | ETH | UP | 0.66 | 0.84 | 1.54 |
