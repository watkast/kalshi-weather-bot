# Range-Scalp Bot

*Updated Thu Oct 08 21:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 7988 | 6918 | 1070 (13) | 1 | $-2535.50 | -5.0% |
| **+10¢** | 6051 | 4782 | 1269 (25) | 1 | $-2517.45 | -6.6% |
| **+15¢** | 5092 | 3757 | 1335 (37) | 0 | $-2036.97 | -6.4% |
| **+20¢** | 4547 | 3163 | 1384 (45) | 0 | $-1614.75 | -5.7% |
| **+10¢ (15¢ stop)** | 9706 | 9676 | 30 (19) | 0 | $-3573.68 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-08 21:02 | +10 stop | SOL | DOWN | 0.67 | 0.78 | 0.81 |
| 10-08 21:02 | +10 stop | XRP | UP | 0.57 | 0.41 | -1.95 |
| 10-08 21:02 | +10 | XRP | UP | 0.57 | open |  |
| 10-08 21:02 | +5 | XRP | UP | 0.57 | open |  |
| 10-08 21:01 | +10 stop | XRP | DOWN | 0.44 | 0.54 | 0.64 |
| 10-08 21:01 | +20 | XRP | DOWN | 0.44 | 0.66 | 1.86 |
| 10-08 21:01 | +15 | XRP | DOWN | 0.44 | 0.66 | 1.86 |
| 10-08 21:01 | +10 | XRP | DOWN | 0.44 | 0.54 | 0.64 |
| 10-08 21:01 | +5 | XRP | DOWN | 0.44 | 0.54 | 0.64 |
| 10-08 21:01 | +10 stop | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 10-08 21:01 | +20 | ETH | DOWN | 0.60 | 0.83 | 2.03 |
| 10-08 21:01 | +15 | ETH | DOWN | 0.61 | 0.77 | 1.30 |
| 10-08 21:01 | +10 | ETH | DOWN | 0.61 | 0.77 | 1.30 |
| 10-08 21:01 | +5 | ETH | DOWN | 0.61 | 0.70 | 0.58 |
| 10-08 21:01 | +10 stop | DOGE | DOWN | 0.62 | 0.78 | 1.30 |
| 10-08 21:01 | +20 | DOGE | DOWN | 0.61 | 0.81 | 1.72 |
| 10-08 21:01 | +15 | DOGE | DOWN | 0.61 | 0.78 | 1.40 |
| 10-08 21:01 | +10 | DOGE | DOWN | 0.61 | 0.78 | 1.40 |
| 10-08 21:01 | +5 | DOGE | DOWN | 0.61 | 0.67 | 0.27 |
| 10-08 21:01 | +10 stop | BNB | DOWN | 0.62 | 0.73 | 0.79 |
| 10-08 21:01 | +20 | BNB | DOWN | 0.61 | 0.82 | 1.78 |
| 10-08 21:01 | +15 | BNB | DOWN | 0.61 | 0.79 | 1.47 |
| 10-08 21:01 | +10 | BNB | DOWN | 0.61 | 0.73 | 0.85 |
| 10-08 21:01 | +5 | BNB | DOWN | 0.62 | 0.70 | 0.48 |
| 10-08 21:01 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 10-08 21:01 | +20 | NEAR | DOWN | 0.67 | 0.94 | 2.47 |
| 10-08 21:01 | +15 | NEAR | DOWN | 0.67 | 0.86 | 1.65 |
| 10-08 21:01 | +10 | NEAR | DOWN | 0.67 | 0.86 | 1.64 |
| 10-08 21:01 | +5 | NEAR | DOWN | 0.67 | 0.77 | 0.70 |
| 10-08 21:01 | +10 stop | ZEC | DOWN | 0.66 | 0.77 | 0.80 |
| 10-08 21:01 | +20 | ZEC | DOWN | 0.66 | 0.88 | 1.95 |
| 10-08 21:01 | +15 | ZEC | DOWN | 0.66 | 0.82 | 1.31 |
| 10-08 21:01 | +10 | ZEC | DOWN | 0.66 | 0.77 | 0.80 |
| 10-08 21:01 | +5 | ZEC | DOWN | 0.66 | 0.73 | 0.38 |
| 10-08 21:01 | +10 stop | SOL | DOWN | 0.68 | 0.53 | -1.84 |
| 10-08 21:01 | +20 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 10-08 21:01 | +15 | SOL | DOWN | 0.68 | 0.83 | 1.24 |
| 10-08 21:01 | +10 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-08 21:01 | +5 | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 10-08 20:57 | +10 stop | ZEC | DOWN | 0.37 | 0.60 | 1.96 |
