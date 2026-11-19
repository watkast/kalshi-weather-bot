# Range-Scalp Bot

*Updated Thu Nov 19 17:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65213 | 56929 | 8284 (124) | 0 | $-17435.82 | -4.2% |
| **+10¢** | 48705 | 39010 | 9695 (165) | 2 | $-16247.56 | -5.3% |
| **+15¢** | 40841 | 30383 | 10458 (211) | 2 | $-14634.24 | -5.7% |
| **+20¢** | 36372 | 25385 | 10987 (266) | 1 | $-12953.90 | -5.7% |
| **+10¢ (15¢ stop)** | 79391 | 79227 | 164 (98) | 2 | $-29226.32 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 17:10 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 11-19 17:10 | +10 | HYPE | DOWN | 0.71 | open |  |
| 11-19 17:10 | +15 | HYPE | DOWN | 0.70 | open |  |
| 11-19 17:10 | +10 stop | ZEC | UP | 0.57 | open |  |
| 11-19 17:10 | +20 | ZEC | UP | 0.59 | open |  |
| 11-19 17:10 | +15 | ZEC | UP | 0.59 | open |  |
| 11-19 17:10 | +10 | ZEC | UP | 0.59 | open |  |
| 11-19 17:10 | +5 | ZEC | UP | 0.58 | 0.65 | 0.36 |
| 11-19 17:08 | +10 stop | ZEC | DOWN | 0.52 | 0.73 | 1.78 |
| 11-19 17:08 | +20 | ZEC | DOWN | 0.53 | 0.73 | 1.68 |
| 11-19 17:08 | +15 | ZEC | DOWN | 0.54 | 0.73 | 1.58 |
| 11-19 17:08 | +10 | ZEC | DOWN | 0.55 | 0.73 | 1.48 |
| 11-19 17:08 | +5 | ZEC | DOWN | 0.53 | 0.73 | 1.69 |
| 11-19 17:02 | +10 stop | ZEC | DOWN | 0.69 | 0.82 | 1.04 |
| 11-19 17:02 | +20 | ZEC | DOWN | 0.67 | 0.87 | 1.76 |
| 11-19 17:02 | +15 | ZEC | DOWN | 0.67 | 0.82 | 1.23 |
| 11-19 17:02 | +10 | ZEC | DOWN | 0.67 | 0.78 | 0.81 |
| 11-19 17:02 | +5 | ZEC | DOWN | 0.67 | 0.74 | 0.40 |
| 11-19 17:01 | +10 stop | DOGE | DOWN | 0.66 | 0.78 | 0.91 |
| 11-19 17:01 | +20 | DOGE | DOWN | 0.64 | 0.84 | 1.73 |
| 11-19 17:01 | +15 | DOGE | DOWN | 0.64 | 0.80 | 1.31 |
| 11-19 17:01 | +10 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-19 17:01 | +5 | DOGE | DOWN | 0.63 | 0.78 | 1.20 |
| 11-19 17:01 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 11-19 17:01 | +20 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
| 11-19 17:01 | +15 | ETH | DOWN | 0.63 | 0.81 | 1.52 |
| 11-19 17:01 | +10 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 11-19 17:01 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.17 |
| 11-19 17:01 | +10 stop | SOL | DOWN | 0.59 | 0.70 | 0.78 |
| 11-19 17:01 | +20 | SOL | DOWN | 0.60 | 0.88 | 2.55 |
| 11-19 17:01 | +15 | SOL | DOWN | 0.60 | 0.76 | 1.30 |
| 11-19 17:01 | +10 | SOL | DOWN | 0.60 | 0.70 | 0.68 |
| 11-19 17:01 | +5 | SOL | DOWN | 0.60 | 0.68 | 0.48 |
| 11-19 17:01 | +10 stop | HYPE | DOWN | 0.54 | 0.69 | 1.17 |
| 11-19 17:01 | +20 | HYPE | DOWN | 0.54 | 0.74 | 1.68 |
| 11-19 17:01 | +15 | HYPE | DOWN | 0.54 | 0.69 | 1.17 |
| 11-19 17:01 | +10 | HYPE | DOWN | 0.54 | 0.69 | 1.17 |
| 11-19 17:01 | +5 | HYPE | DOWN | 0.54 | 0.60 | 0.25 |
| 11-19 17:01 | +10 stop | XRP | DOWN | 0.62 | 0.73 | 0.79 |
| 11-19 17:01 | +20 | XRP | DOWN | 0.62 | 0.83 | 1.83 |
