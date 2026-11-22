# Range-Scalp Bot

*Updated Sun Nov 22 19:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69020 | 60230 | 8790 (145) | 0 | $-18541.92 | -4.3% |
| **+10¢** | 51504 | 41240 | 10264 (188) | 0 | $-17176.71 | -5.3% |
| **+15¢** | 43165 | 32100 | 11065 (240) | 0 | $-15413.50 | -5.7% |
| **+20¢** | 38433 | 26806 | 11627 (299) | 2 | $-13706.55 | -5.7% |
| **+10¢ (15¢ stop)** | 84033 | 83844 | 189 (117) | 0 | $-30942.48 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 19:34 | +10 stop | BTC | DOWN | 0.68 | 0.82 | 1.13 |
| 11-22 19:34 | +10 | BTC | DOWN | 0.68 | 0.82 | 1.13 |
| 11-22 19:34 | +5 | BTC | DOWN | 0.68 | 0.77 | 0.61 |
| 11-22 19:34 | +10 stop | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-22 19:34 | +20 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-22 19:34 | +15 | ZEC | DOWN | 0.63 | 0.83 | 1.73 |
| 11-22 19:34 | +10 | ZEC | DOWN | 0.63 | 0.76 | 1.00 |
| 11-22 19:34 | +5 | ZEC | DOWN | 0.64 | 0.76 | 0.90 |
| 11-22 19:33 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 11-22 19:31 | +10 stop | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-22 19:31 | +20 | BTC | DOWN | 0.69 | open |  |
| 11-22 19:31 | +15 | BTC | DOWN | 0.69 | 0.85 | 1.36 |
| 11-22 19:31 | +10 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-22 19:31 | +5 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-22 19:31 | +10 stop | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-22 19:31 | +20 | DOGE | DOWN | 0.69 | open |  |
| 11-22 19:31 | +15 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-22 19:31 | +10 | DOGE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-22 19:31 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 11-22 19:30 | +10 stop | NEAR | DOWN | 0.65 | 0.77 | 0.91 |
| 11-22 19:30 | +20 | NEAR | DOWN | 0.65 | 0.89 | 2.17 |
| 11-22 19:30 | +15 | NEAR | DOWN | 0.66 | 0.81 | 1.23 |
| 11-22 19:30 | +10 | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 11-22 19:30 | +5 | NEAR | DOWN | 0.66 | 0.73 | 0.40 |
| 11-22 19:30 | +10 stop | ETH | DOWN | 0.53 | 0.63 | 0.65 |
| 11-22 19:30 | +20 | ETH | DOWN | 0.53 | 0.76 | 1.99 |
| 11-22 19:30 | +15 | ETH | DOWN | 0.53 | 0.69 | 1.27 |
| 11-22 19:30 | +10 | ETH | DOWN | 0.53 | 0.63 | 0.65 |
| 11-22 19:30 | +5 | ETH | DOWN | 0.53 | 0.63 | 0.65 |
| 11-22 19:30 | +10 stop | XRP | DOWN | 0.53 | 0.70 | 1.37 |
| 11-22 19:30 | +20 | XRP | DOWN | 0.53 | 0.78 | 2.19 |
| 11-22 19:30 | +15 | XRP | DOWN | 0.52 | 0.70 | 1.47 |
| 11-22 19:30 | +10 | XRP | DOWN | 0.52 | 0.70 | 1.47 |
| 11-22 19:30 | +5 | XRP | DOWN | 0.52 | 0.57 | 0.14 |
| 11-22 19:30 | +10 stop | HYPE | DOWN | 0.58 | 0.75 | 1.38 |
| 11-22 19:30 | +20 | HYPE | DOWN | 0.58 | 0.78 | 1.69 |
| 11-22 19:30 | +15 | HYPE | DOWN | 0.54 | 0.75 | 1.78 |
| 11-22 19:30 | +10 | HYPE | DOWN | 0.54 | 0.75 | 1.78 |
| 11-22 19:30 | +5 | HYPE | DOWN | 0.54 | 0.59 | 0.15 |
| 11-22 19:30 | +10 stop | SOL | DOWN | 0.52 | 0.73 | 1.78 |
