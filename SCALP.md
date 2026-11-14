# Range-Scalp Bot

*Updated Sat Nov 14 19:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59787 | 52166 | 7621 (107) | 1 | $-16169.79 | -4.3% |
| **+10¢** | 44663 | 35739 | 8924 (143) | 2 | $-15198.72 | -5.4% |
| **+15¢** | 37421 | 27798 | 9623 (180) | 2 | $-13829.58 | -5.9% |
| **+20¢** | 33339 | 23241 | 10098 (232) | 2 | $-12172.74 | -5.8% |
| **+10¢ (15¢ stop)** | 72758 | 72615 | 143 (82) | 0 | $-26747.46 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 19:56 | +5 | HYPE | DOWN | 0.65 | 0.70 | 0.19 |
| 11-14 19:54 | +10 stop | NEAR | DOWN | 0.60 | 0.72 | 0.88 |
| 11-14 19:54 | +10 stop | BNB | DOWN | 0.64 | 0.76 | 0.90 |
| 11-14 19:54 | +20 | BNB | DOWN | 0.64 | 0.92 | 2.59 |
| 11-14 19:54 | +15 | BNB | DOWN | 0.64 | 0.92 | 2.59 |
| 11-14 19:54 | +10 | BNB | DOWN | 0.65 | 0.76 | 0.80 |
| 11-14 19:54 | +5 | BNB | DOWN | 0.67 | 0.76 | 0.61 |
| 11-14 19:54 | +5 | NEAR | DOWN | 0.52 | 0.58 | 0.21 |
| 11-14 19:53 | +10 stop | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-14 19:53 | +10 | HYPE | DOWN | 0.57 | 0.67 | 0.66 |
| 11-14 19:53 | +5 | HYPE | DOWN | 0.57 | 0.63 | 0.25 |
| 11-14 19:53 | +5 | NEAR | DOWN | 0.59 | 0.66 | 0.34 |
| 11-14 19:52 | +10 stop | NEAR | DOWN | 0.69 | 0.53 | -1.94 |
| 11-14 19:51 | +5 | NEAR | DOWN | 0.71 | 0.79 | 0.54 |
| 11-14 19:50 | +10 stop | HYPE | DOWN | 0.61 | 0.75 | 1.12 |
| 11-14 19:50 | +10 | HYPE | DOWN | 0.61 | 0.75 | 1.12 |
| 11-14 19:50 | +5 | HYPE | DOWN | 0.59 | 0.68 | 0.57 |
| 11-14 19:50 | +10 stop | NEAR | DOWN | 0.47 | 0.65 | 1.44 |
| 11-14 19:50 | +5 | NEAR | DOWN | 0.48 | 0.56 | 0.44 |
| 11-14 19:47 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-14 19:47 | +20 | SOL | DOWN | 0.71 | 0.91 | 1.83 |
| 11-14 19:47 | +15 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 11-14 19:47 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-14 19:47 | +5 | SOL | DOWN | 0.68 | 0.77 | 0.61 |
| 11-14 19:47 | +10 stop | XRP | DOWN | 0.68 | 0.79 | 0.82 |
| 11-14 19:46 | +5 | NEAR | DOWN | 0.71 | 0.78 | 0.42 |
| 11-14 19:46 | +10 stop | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 11-14 19:46 | +20 | HYPE | DOWN | 0.67 | 0.90 | 2.11 |
| 11-14 19:46 | +15 | HYPE | DOWN | 0.67 | 0.85 | 1.55 |
| 11-14 19:46 | +10 | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 11-14 19:46 | +5 | HYPE | DOWN | 0.67 | 0.73 | 0.30 |
| 11-14 19:46 | +10 stop | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 11-14 19:46 | +20 | BNB | DOWN | 0.62 | 0.83 | 1.83 |
| 11-14 19:46 | +15 | BNB | DOWN | 0.62 | 0.83 | 1.83 |
| 11-14 19:46 | +10 | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 11-14 19:46 | +5 | BNB | DOWN | 0.62 | 0.70 | 0.48 |
| 11-14 19:46 | +10 stop | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-14 19:46 | +20 | BTC | DOWN | 0.71 | 0.92 | 1.88 |
| 11-14 19:46 | +15 | BTC | DOWN | 0.71 | 0.86 | 1.26 |
| 11-14 19:46 | +10 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
