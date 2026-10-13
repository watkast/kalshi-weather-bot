# Range-Scalp Bot

*Updated Tue Oct 13 12:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14617 | 12639 | 1978 (27) | 0 | $-4739.12 | -5.1% |
| **+10¢** | 11066 | 8771 | 2295 (39) | 0 | $-4429.90 | -6.4% |
| **+15¢** | 9301 | 6847 | 2454 (57) | 1 | $-3934.18 | -6.7% |
| **+20¢** | 8274 | 5718 | 2556 (72) | 3 | $-3391.84 | -6.5% |
| **+10¢ (15¢ stop)** | 17953 | 17904 | 49 (29) | 0 | $-6988.80 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 12:17 | +10 stop | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-13 12:17 | +20 | DOGE | DOWN | 0.65 | open |  |
| 10-13 12:17 | +15 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-13 12:17 | +10 | DOGE | DOWN | 0.65 | 0.77 | 0.91 |
| 10-13 12:17 | +5 | DOGE | DOWN | 0.65 | 0.72 | 0.39 |
| 10-13 12:17 | +10 stop | SOL | DOWN | 0.69 | 0.80 | 0.78 |
| 10-13 12:17 | +20 | SOL | DOWN | 0.69 | 0.90 | 1.85 |
| 10-13 12:17 | +15 | SOL | DOWN | 0.69 | 0.87 | 1.52 |
| 10-13 12:17 | +10 | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-13 12:17 | +5 | SOL | DOWN | 0.68 | 0.80 | 0.92 |
| 10-13 12:16 | +10 stop | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-13 12:16 | +20 | ETH | DOWN | 0.71 | open |  |
| 10-13 12:16 | +15 | ETH | DOWN | 0.71 | open |  |
| 10-13 12:16 | +10 | ETH | DOWN | 0.71 | 0.81 | 0.74 |
| 10-13 12:16 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
| 10-13 12:16 | +10 stop | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-13 12:16 | +20 | ZEC | DOWN | 0.69 | open |  |
| 10-13 12:16 | +15 | ZEC | DOWN | 0.69 | 0.84 | 1.25 |
| 10-13 12:16 | +10 | ZEC | DOWN | 0.69 | 0.80 | 0.83 |
| 10-13 12:16 | +5 | ZEC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-13 12:12 | +10 stop | NEAR | DOWN | 0.44 | 0.61 | 1.35 |
| 10-13 12:12 | +10 | NEAR | DOWN | 0.45 | 0.61 | 1.25 |
| 10-13 12:12 | +5 | NEAR | DOWN | 0.44 | 0.61 | 1.35 |
| 10-13 12:12 | +10 stop | SOL | DOWN | 0.44 | 0.54 | 0.64 |
| 10-13 12:11 | +10 stop | DOGE | DOWN | 0.64 | 0.76 | 0.90 |
| 10-13 12:11 | +10 stop | BNB | DOWN | 0.59 | 0.84 | 2.23 |
| 10-13 12:10 | +10 stop | NEAR | DOWN | 0.65 | 0.78 | 1.01 |
| 10-13 12:10 | +20 | NEAR | DOWN | 0.65 | 0.85 | 1.75 |
| 10-13 12:10 | +15 | NEAR | DOWN | 0.65 | 0.85 | 1.75 |
| 10-13 12:10 | +10 | NEAR | DOWN | 0.65 | 0.78 | 1.01 |
| 10-13 12:10 | +5 | NEAR | DOWN | 0.65 | 0.70 | 0.19 |
| 10-13 12:10 | +10 stop | SOL | UP | 0.63 | 0.41 | -2.54 |
| 10-13 12:10 | +10 stop | BTC | DOWN | 0.58 | 0.76 | 1.49 |
| 10-13 12:10 | +10 | BTC | DOWN | 0.59 | 0.76 | 1.40 |
| 10-13 12:10 | +5 | BTC | DOWN | 0.58 | 0.64 | 0.25 |
| 10-13 12:10 | +10 stop | ETH | DOWN | 0.59 | 0.73 | 1.09 |
| 10-13 12:10 | +10 | ETH | DOWN | 0.59 | 0.73 | 1.09 |
| 10-13 12:10 | +5 | ETH | DOWN | 0.58 | 0.65 | 0.36 |
| 10-13 12:09 | +10 stop | DOGE | DOWN | 0.65 | 0.49 | -1.94 |
| 10-13 12:09 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.19 |
