# Range-Scalp Bot

*Updated Fri Nov 13 21:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 58664 | 51188 | 7476 (105) | 0 | $-15825.92 | -4.3% |
| **+10¢** | 43824 | 35080 | 8744 (139) | 0 | $-14797.38 | -5.4% |
| **+15¢** | 36726 | 27307 | 9419 (174) | 2 | $-13385.41 | -5.8% |
| **+20¢** | 32718 | 22830 | 9888 (225) | 2 | $-11771.94 | -5.7% |
| **+10¢ (15¢ stop)** | 71432 | 71298 | 134 (82) | 0 | $-26294.47 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-13 21:02 | +10 stop | NEAR | DOWN | 0.67 | 0.78 | 0.81 |
| 11-13 21:02 | +20 | NEAR | DOWN | 0.68 | open |  |
| 11-13 21:02 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-13 21:02 | +10 | NEAR | DOWN | 0.68 | 0.78 | 0.76 |
| 11-13 21:02 | +5 | NEAR | DOWN | 0.68 | 0.74 | 0.30 |
| 11-13 21:01 | +10 stop | BTC | DOWN | 0.66 | 0.82 | 1.33 |
| 11-13 21:01 | +20 | BTC | DOWN | 0.66 | open |  |
| 11-13 21:01 | +15 | BTC | DOWN | 0.69 | open |  |
| 11-13 21:01 | +10 | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-13 21:01 | +5 | BTC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-13 21:01 | +10 stop | ETH | DOWN | 0.58 | 0.69 | 0.77 |
| 11-13 21:01 | +20 | ETH | DOWN | 0.58 | 0.83 | 2.22 |
| 11-13 21:01 | +15 | ETH | DOWN | 0.58 | 0.83 | 2.22 |
| 11-13 21:01 | +10 | ETH | DOWN | 0.58 | 0.69 | 0.77 |
| 11-13 21:01 | +5 | ETH | DOWN | 0.58 | 0.69 | 0.77 |
| 11-13 21:00 | +10 stop | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 11-13 21:00 | +20 | BNB | DOWN | 0.61 | 0.82 | 1.82 |
| 11-13 21:00 | +15 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 11-13 21:00 | +10 | BNB | DOWN | 0.61 | 0.76 | 1.20 |
| 11-13 21:00 | +5 | BNB | DOWN | 0.61 | 0.67 | 0.27 |
| 11-13 21:00 | +10 stop | HYPE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-13 21:00 | +20 | HYPE | DOWN | 0.66 | 0.87 | 1.86 |
| 11-13 21:00 | +15 | HYPE | DOWN | 0.66 | 0.87 | 1.86 |
| 11-13 21:00 | +10 | HYPE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-13 21:00 | +5 | HYPE | DOWN | 0.66 | 0.72 | 0.29 |
| 11-13 20:58 | +10 stop | BNB | UP | 0.71 | 0.52 | -2.23 |
| 11-13 20:58 | +20 | BNB | UP | 0.71 | 1.00 | 2.72 |
| 11-13 20:58 | +15 | BNB | UP | 0.71 | 1.00 | 2.72 |
| 11-13 20:58 | +10 | BNB | UP | 0.71 | 1.00 | 2.72 |
| 11-13 20:58 | +5 | BNB | UP | 0.71 | 0.79 | 0.53 |
| 11-13 20:58 | +10 stop | ETH | UP | 0.65 | 0.79 | 1.12 |
| 11-13 20:58 | +20 | ETH | UP | 0.62 | 0.95 | 3.05 |
| 11-13 20:58 | +15 | ETH | UP | 0.65 | 0.95 | 2.76 |
| 11-13 20:58 | +10 | ETH | UP | 0.65 | 0.79 | 1.12 |
| 11-13 20:58 | +5 | ETH | UP | 0.65 | 0.79 | 1.12 |
| 11-13 20:57 | +5 | XRP | UP | 0.53 | 0.59 | 0.25 |
| 11-13 20:56 | +10 stop | BTC | DOWN | 0.59 | 0.93 | 3.19 |
| 11-13 20:56 | +10 stop | XRP | UP | 0.64 | 0.35 | -3.23 |
| 11-13 20:56 | +10 | XRP | UP | 0.63 | no | -6.47 |
| 11-13 20:56 | +5 | XRP | UP | 0.63 | 0.70 | 0.38 |
