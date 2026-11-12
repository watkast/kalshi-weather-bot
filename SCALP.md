# Range-Scalp Bot

*Updated Thu Nov 12 19:39 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57181 | 49850 | 7331 (101) | 1 | $-15714.18 | -4.4% |
| **+10¢** | 42744 | 34188 | 8556 (133) | 1 | $-14654.43 | -5.5% |
| **+15¢** | 35835 | 26625 | 9210 (167) | 2 | $-13255.32 | -5.9% |
| **+20¢** | 31927 | 22264 | 9663 (217) | 2 | $-11618.41 | -5.8% |
| **+10¢ (15¢ stop)** | 69734 | 69606 | 128 (78) | 1 | $-25728.07 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 19:39 | +10 stop | XRP | UP | 0.68 | open |  |
| 11-12 19:38 | +10 stop | XRP | DOWN | 0.48 | 0.59 | 0.75 |
| 11-12 19:37 | +10 stop | HYPE | DOWN | 0.64 | 0.76 | 0.90 |
| 11-12 19:36 | +10 stop | XRP | UP | 0.58 | 0.43 | -1.86 |
| 11-12 19:36 | +10 stop | ZEC | DOWN | 0.60 | 0.76 | 1.30 |
| 11-12 19:35 | +10 stop | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-12 19:35 | +20 | DOGE | DOWN | 0.71 | 0.95 | 2.20 |
| 11-12 19:35 | +15 | DOGE | DOWN | 0.71 | 0.86 | 1.26 |
| 11-12 19:35 | +10 | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 11-12 19:35 | +5 | DOGE | DOWN | 0.71 | 0.78 | 0.42 |
| 11-12 19:35 | +10 stop | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-12 19:35 | +20 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 11-12 19:35 | +15 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 11-12 19:35 | +10 | SOL | DOWN | 0.67 | 0.79 | 0.92 |
| 11-12 19:35 | +5 | SOL | DOWN | 0.67 | 0.74 | 0.40 |
| 11-12 19:35 | +10 stop | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 11-12 19:35 | +20 | ETH | DOWN | 0.60 | 0.83 | 2.03 |
| 11-12 19:35 | +15 | ETH | DOWN | 0.60 | 0.79 | 1.61 |
| 11-12 19:35 | +10 | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 11-12 19:35 | +5 | ETH | DOWN | 0.60 | 0.66 | 0.27 |
| 11-12 19:35 | +10 stop | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-12 19:35 | +15 | BTC | DOWN | 0.63 | 0.82 | 1.62 |
| 11-12 19:35 | +10 | BTC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-12 19:35 | +5 | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-12 19:35 | +10 stop | ZEC | UP | 0.65 | 0.44 | -2.44 |
| 11-12 19:35 | +10 stop | HYPE | UP | 0.69 | 0.54 | -1.83 |
| 11-12 19:34 | +10 stop | XRP | DOWN | 0.59 | 0.36 | -2.64 |
| 11-12 19:34 | +10 | XRP | DOWN | 0.59 | open |  |
| 11-12 19:34 | +5 | XRP | DOWN | 0.59 | open |  |
| 11-12 19:33 | +5 | HYPE | DOWN | 0.64 | 0.71 | 0.38 |
| 11-12 19:32 | +10 stop | ZEC | DOWN | 0.68 | 0.51 | -2.04 |
| 11-12 19:32 | +20 | ZEC | DOWN | 0.68 | open |  |
| 11-12 19:32 | +15 | ZEC | DOWN | 0.68 | open |  |
| 11-12 19:32 | +10 | ZEC | DOWN | 0.68 | 0.79 | 0.82 |
| 11-12 19:32 | +5 | ZEC | DOWN | 0.68 | 0.76 | 0.51 |
| 11-12 19:32 | +10 stop | HYPE | DOWN | 0.62 | 0.35 | -3.03 |
| 11-12 19:32 | +20 | HYPE | DOWN | 0.60 | 0.82 | 1.92 |
| 11-12 19:32 | +15 | HYPE | DOWN | 0.60 | 0.76 | 1.34 |
| 11-12 19:32 | +10 | HYPE | DOWN | 0.60 | 0.71 | 0.82 |
| 11-12 19:32 | +5 | HYPE | DOWN | 0.60 | 0.67 | 0.41 |
