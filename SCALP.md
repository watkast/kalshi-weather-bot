# Range-Scalp Bot

*Updated Thu Nov 12 20:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57204 | 49873 | 7331 (101) | 2 | $-15705.26 | -4.4% |
| **+10¢** | 42761 | 34204 | 8557 (133) | 2 | $-14643.76 | -5.4% |
| **+15¢** | 35850 | 26638 | 9212 (167) | 1 | $-13249.21 | -5.9% |
| **+20¢** | 31942 | 22277 | 9665 (217) | 1 | $-11606.04 | -5.8% |
| **+10¢ (15¢ stop)** | 69756 | 69628 | 128 (78) | 0 | $-25724.40 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 20:08 | +10 stop | ETH | DOWN | 0.50 | 0.29 | -2.43 |
| 11-12 20:08 | +5 | ETH | DOWN | 0.50 | open |  |
| 11-12 20:07 | +10 stop | ETH | DOWN | 0.56 | 0.71 | 1.17 |
| 11-12 20:06 | +10 stop | XRP | DOWN | 0.67 | 0.82 | 1.24 |
| 11-12 20:06 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-12 20:06 | +20 | BTC | DOWN | 0.69 | 0.93 | 2.22 |
| 11-12 20:06 | +15 | BTC | DOWN | 0.69 | 0.86 | 1.46 |
| 11-12 20:06 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-12 20:06 | +5 | BTC | DOWN | 0.69 | 0.74 | 0.21 |
| 11-12 20:06 | +10 stop | SOL | DOWN | 0.66 | 0.78 | 0.91 |
| 11-12 20:06 | +20 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 11-12 20:06 | +15 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 11-12 20:06 | +10 | SOL | DOWN | 0.66 | 0.78 | 0.91 |
| 11-12 20:06 | +5 | SOL | DOWN | 0.66 | 0.73 | 0.40 |
| 11-12 20:04 | +10 stop | HYPE | UP | 0.57 | 0.41 | -1.95 |
| 11-12 20:04 | +10 | HYPE | UP | 0.57 | open |  |
| 11-12 20:04 | +5 | HYPE | UP | 0.57 | open |  |
| 11-12 20:04 | +10 stop | HYPE | DOWN | 0.42 | 0.53 | 0.74 |
| 11-12 20:04 | +20 | HYPE | DOWN | 0.41 | 0.61 | 1.66 |
| 11-12 20:04 | +15 | HYPE | DOWN | 0.42 | 0.58 | 1.24 |
| 11-12 20:04 | +10 | HYPE | DOWN | 0.42 | 0.53 | 0.74 |
| 11-12 20:04 | +5 | HYPE | DOWN | 0.41 | 0.53 | 0.85 |
| 11-12 20:04 | +10 stop | XRP | DOWN | 0.70 | 0.52 | -2.13 |
| 11-12 20:04 | +20 | XRP | DOWN | 0.70 | 0.91 | 1.89 |
| 11-12 20:04 | +15 | XRP | DOWN | 0.70 | 0.91 | 1.89 |
| 11-12 20:04 | +10 | XRP | DOWN | 0.71 | 0.82 | 0.84 |
| 11-12 20:04 | +5 | XRP | DOWN | 0.71 | 0.76 | 0.22 |
| 11-12 20:04 | +10 stop | ETH | DOWN | 0.66 | 0.51 | -1.84 |
| 11-12 20:04 | +10 | ETH | DOWN | 0.66 | open |  |
| 11-12 20:04 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 11-12 20:01 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-12 20:01 | +20 | ETH | DOWN | 0.68 | open |  |
| 11-12 20:01 | +15 | ETH | DOWN | 0.68 | open |  |
| 11-12 20:01 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-12 20:01 | +5 | ETH | DOWN | 0.67 | 0.75 | 0.50 |
| 11-12 19:50 | +5 | BTC | UP | 0.64 | 0.69 | 0.18 |
| 11-12 19:49 | +5 | BNB | UP | 0.65 | 0.77 | 0.92 |
| 11-12 19:49 | +10 stop | XRP | UP | 0.68 | 0.84 | 1.35 |
| 11-12 19:49 | +10 | XRP | UP | 0.68 | 0.84 | 1.35 |
| 11-12 19:49 | +5 | XRP | UP | 0.68 | 0.74 | 0.31 |
