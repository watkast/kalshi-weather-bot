# Range-Scalp Bot

*Updated Thu Nov 05 15:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48517 | 42277 | 6240 (73) | 1 | $-13791.90 | -4.5% |
| **+10¢** | 36217 | 28969 | 7248 (99) | 2 | $-12619.73 | -5.5% |
| **+15¢** | 30337 | 22530 | 7807 (127) | 3 | $-11524.69 | -6.1% |
| **+20¢** | 26952 | 18771 | 8181 (166) | 5 | $-10190.23 | -6.0% |
| **+10¢ (15¢ stop)** | 59117 | 59024 | 93 (56) | 2 | $-21902.52 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 15:50 | +10 stop | HYPE | DOWN | 0.67 | open |  |
| 11-05 15:49 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 11-05 15:49 | +5 | ETH | DOWN | 0.65 | 0.71 | 0.27 |
| 11-05 15:48 | +10 stop | ZEC | DOWN | 0.62 | 0.77 | 1.20 |
| 11-05 15:48 | +5 | XRP | DOWN | 0.60 | 0.68 | 0.47 |
| 11-05 15:48 | +5 | DOGE | DOWN | 0.57 | 0.71 | 1.07 |
| 11-05 15:47 | +10 stop | HYPE | UP | 0.55 | 0.70 | 1.17 |
| 11-05 15:47 | +5 | XRP | DOWN | 0.62 | 0.67 | 0.17 |
| 11-05 15:47 | +5 | ETH | DOWN | 0.58 | 0.63 | 0.15 |
| 11-05 15:47 | +5 | DOGE | DOWN | 0.59 | 0.67 | 0.47 |
| 11-05 15:47 | +5 | SOL | DOWN | 0.62 | 0.76 | 1.10 |
| 11-05 15:47 | +5 | ETH | DOWN | 0.54 | 0.60 | 0.26 |
| 11-05 15:46 | +10 stop | BTC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-05 15:46 | +20 | BTC | DOWN | 0.66 | open |  |
| 11-05 15:46 | +15 | BTC | DOWN | 0.66 | open |  |
| 11-05 15:46 | +10 | BTC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-05 15:46 | +5 | BTC | DOWN | 0.66 | 0.79 | 1.02 |
| 11-05 15:46 | +10 stop | XRP | DOWN | 0.65 | 0.78 | 1.01 |
| 11-05 15:46 | +20 | XRP | DOWN | 0.65 | 0.85 | 1.75 |
| 11-05 15:46 | +15 | XRP | DOWN | 0.65 | 0.83 | 1.54 |
| 11-05 15:46 | +10 | XRP | DOWN | 0.65 | 0.78 | 1.01 |
| 11-05 15:46 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
| 11-05 15:46 | +10 stop | ZEC | DOWN | 0.71 | 0.56 | -1.83 |
| 11-05 15:46 | +20 | ZEC | DOWN | 0.71 | open |  |
| 11-05 15:46 | +15 | ZEC | DOWN | 0.71 | 0.88 | 1.47 |
| 11-05 15:46 | +10 | ZEC | DOWN | 0.71 | 0.88 | 1.47 |
| 11-05 15:46 | +5 | ZEC | DOWN | 0.71 | 0.77 | 0.32 |
| 11-05 15:46 | +10 stop | SOL | DOWN | 0.63 | 0.76 | 1.00 |
| 11-05 15:46 | +20 | SOL | DOWN | 0.61 | open |  |
| 11-05 15:46 | +15 | SOL | DOWN | 0.61 | 0.76 | 1.20 |
| 11-05 15:46 | +10 | SOL | DOWN | 0.61 | 0.76 | 1.20 |
| 11-05 15:46 | +5 | SOL | DOWN | 0.61 | 0.70 | 0.58 |
| 11-05 15:46 | +10 stop | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 11-05 15:46 | +20 | ETH | DOWN | 0.64 | 0.85 | 1.84 |
| 11-05 15:46 | +15 | ETH | DOWN | 0.64 | 0.85 | 1.84 |
| 11-05 15:46 | +10 | ETH | DOWN | 0.64 | 0.77 | 1.00 |
| 11-05 15:46 | +5 | ETH | DOWN | 0.64 | 0.72 | 0.48 |
| 11-05 15:46 | +10 stop | DOGE | DOWN | 0.58 | 0.71 | 0.97 |
| 11-05 15:46 | +20 | DOGE | DOWN | 0.59 | 0.80 | 1.81 |
| 11-05 15:46 | +15 | DOGE | DOWN | 0.58 | 0.77 | 1.59 |
