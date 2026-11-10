# Range-Scalp Bot

*Updated Tue Nov 10 06:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54265 | 47334 | 6931 (89) | 0 | $-14795.83 | -4.3% |
| **+10¢** | 40550 | 32465 | 8085 (117) | 0 | $-13726.24 | -5.4% |
| **+15¢** | 33987 | 25270 | 8717 (150) | 0 | $-12496.47 | -5.9% |
| **+20¢** | 30267 | 21122 | 9145 (198) | 0 | $-10903.66 | -5.7% |
| **+10¢ (15¢ stop)** | 66113 | 66003 | 110 (66) | 0 | $-24430.45 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 06:05 | +10 stop | HYPE | DOWN | 0.60 | 0.77 | 1.40 |
| 11-10 06:05 | +5 | HYPE | DOWN | 0.60 | 0.77 | 1.40 |
| 11-10 06:05 | +10 stop | BNB | DOWN | 0.69 | 0.79 | 0.73 |
| 11-10 06:05 | +10 stop | NEAR | DOWN | 0.59 | 0.70 | 0.78 |
| 11-10 06:03 | +10 stop | HYPE | DOWN | 0.67 | 0.51 | -1.96 |
| 11-10 06:03 | +20 | HYPE | DOWN | 0.67 | 0.87 | 1.76 |
| 11-10 06:03 | +15 | HYPE | DOWN | 0.67 | 0.87 | 1.76 |
| 11-10 06:03 | +10 | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-10 06:03 | +5 | HYPE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-10 06:02 | +10 stop | BNB | DOWN | 0.69 | 0.51 | -2.13 |
| 11-10 06:02 | +20 | BNB | DOWN | 0.69 | 0.91 | 1.93 |
| 11-10 06:02 | +15 | BNB | DOWN | 0.66 | 0.88 | 1.96 |
| 11-10 06:02 | +10 | BNB | DOWN | 0.66 | 0.79 | 1.02 |
| 11-10 06:02 | +5 | BNB | DOWN | 0.66 | 0.71 | 0.19 |
| 11-10 06:02 | +10 stop | NEAR | DOWN | 0.69 | 0.52 | -2.03 |
| 11-10 06:02 | +20 | NEAR | DOWN | 0.69 | 0.92 | 2.07 |
| 11-10 06:02 | +15 | NEAR | DOWN | 0.69 | 0.92 | 2.07 |
| 11-10 06:02 | +10 | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 11-10 06:02 | +5 | NEAR | DOWN | 0.69 | 0.81 | 0.94 |
| 11-10 06:00 | +10 stop | XRP | DOWN | 0.62 | 0.73 | 0.79 |
| 11-10 06:00 | +20 | XRP | DOWN | 0.62 | 0.85 | 2.04 |
| 11-10 06:00 | +15 | XRP | DOWN | 0.62 | 0.85 | 2.04 |
| 11-10 06:00 | +10 | XRP | DOWN | 0.62 | 0.73 | 0.79 |
| 11-10 06:00 | +5 | XRP | DOWN | 0.62 | 0.73 | 0.79 |
| 11-10 05:58 | +10 stop | HYPE | UP | 0.37 | 0.58 | 1.75 |
| 11-10 05:58 | +10 | HYPE | UP | 0.37 | 0.58 | 1.75 |
| 11-10 05:58 | +5 | HYPE | UP | 0.37 | 0.58 | 1.75 |
| 11-10 05:57 | +10 stop | HYPE | DOWN | 0.43 | 0.55 | 0.84 |
| 11-10 05:57 | +10 | HYPE | DOWN | 0.43 | 0.55 | 0.84 |
| 11-10 05:57 | +5 | HYPE | DOWN | 0.43 | 0.55 | 0.84 |
| 11-10 05:57 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-10 05:57 | +20 | ETH | DOWN | 0.65 | 0.95 | 2.82 |
| 11-10 05:57 | +15 | ETH | DOWN | 0.64 | 0.82 | 1.52 |
| 11-10 05:57 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-10 05:57 | +5 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-10 05:57 | +10 stop | ZEC | UP | 0.52 | 0.63 | 0.75 |
| 11-10 05:57 | +20 | ZEC | UP | 0.52 | 0.72 | 1.67 |
| 11-10 05:57 | +15 | ZEC | UP | 0.52 | 0.72 | 1.67 |
| 11-10 05:57 | +10 | ZEC | UP | 0.54 | 0.72 | 1.47 |
| 11-10 05:57 | +5 | ZEC | UP | 0.55 | 0.63 | 0.45 |
