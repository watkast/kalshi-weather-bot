# Range-Scalp Bot

*Updated Sat Nov 21 02:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 66940 | 58425 | 8515 (128) | 0 | $-17971.37 | -4.3% |
| **+10¢** | 49987 | 40034 | 9953 (170) | 0 | $-16709.01 | -5.3% |
| **+15¢** | 41917 | 31186 | 10731 (217) | 0 | $-15005.89 | -5.7% |
| **+20¢** | 37309 | 26034 | 11275 (274) | 0 | $-13326.69 | -5.7% |
| **+10¢ (15¢ stop)** | 81495 | 81329 | 166 (100) | 0 | $-30019.76 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-21 02:32 | +5 | BTC | DOWN | 0.65 | 0.73 | 0.50 |
| 11-21 02:31 | +10 stop | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 11-21 02:31 | +20 | SOL | DOWN | 0.70 | 0.91 | 1.93 |
| 11-21 02:31 | +15 | SOL | DOWN | 0.70 | 0.89 | 1.68 |
| 11-21 02:31 | +10 | SOL | DOWN | 0.70 | 0.83 | 1.05 |
| 11-21 02:31 | +5 | SOL | DOWN | 0.70 | 0.79 | 0.63 |
| 11-21 02:31 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-21 02:31 | +20 | HYPE | DOWN | 0.59 | 0.84 | 2.23 |
| 11-21 02:31 | +15 | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 11-21 02:31 | +10 | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-21 02:31 | +5 | HYPE | DOWN | 0.59 | 0.65 | 0.27 |
| 11-21 02:31 | +10 stop | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-21 02:31 | +20 | BTC | DOWN | 0.61 | 0.86 | 2.24 |
| 11-21 02:31 | +15 | BTC | DOWN | 0.61 | 0.86 | 2.24 |
| 11-21 02:31 | +10 | BTC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-21 02:31 | +5 | BTC | DOWN | 0.61 | 0.66 | 0.17 |
| 11-21 02:31 | +10 stop | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-21 02:31 | +20 | ZEC | DOWN | 0.69 | 0.93 | 2.22 |
| 11-21 02:31 | +15 | ZEC | DOWN | 0.69 | 0.88 | 1.67 |
| 11-21 02:31 | +10 | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-21 02:31 | +5 | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-21 02:31 | +10 stop | ETH | DOWN | 0.63 | 0.80 | 1.41 |
| 11-21 02:31 | +20 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
| 11-21 02:31 | +15 | ETH | DOWN | 0.63 | 0.80 | 1.41 |
| 11-21 02:31 | +10 | ETH | DOWN | 0.63 | 0.80 | 1.41 |
| 11-21 02:31 | +5 | ETH | DOWN | 0.63 | 0.72 | 0.58 |
| 11-21 02:27 | +5 | HYPE | UP | 0.51 | 0.59 | 0.45 |
| 11-21 02:27 | +10 stop | HYPE | UP | 0.55 | 0.26 | -3.22 |
| 11-21 02:27 | +5 | HYPE | UP | 0.53 | 0.60 | 0.35 |
| 11-21 02:25 | +5 | HYPE | UP | 0.58 | 0.64 | 0.25 |
| 11-21 02:25 | +10 stop | NEAR | UP | 0.62 | 0.78 | 1.30 |
| 11-21 02:25 | +10 stop | DOGE | UP | 0.63 | 0.75 | 0.89 |
| 11-21 02:25 | +10 stop | HYPE | DOWN | 0.47 | 0.32 | -1.84 |
| 11-21 02:25 | +10 | HYPE | DOWN | 0.47 | 0.73 | 2.28 |
| 11-21 02:25 | +5 | HYPE | DOWN | 0.47 | 0.52 | 0.14 |
| 11-21 02:24 | +10 stop | HYPE | DOWN | 0.55 | 0.65 | 0.66 |
| 11-21 02:24 | +15 | HYPE | DOWN | 0.55 | 0.73 | 1.48 |
| 11-21 02:24 | +10 | HYPE | DOWN | 0.55 | 0.65 | 0.66 |
| 11-21 02:24 | +5 | HYPE | DOWN | 0.55 | 0.65 | 0.66 |
| 11-21 02:23 | +5 | DOGE | DOWN | 0.61 | 0.67 | 0.27 |
