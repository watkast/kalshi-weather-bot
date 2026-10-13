# Range-Scalp Bot

*Updated Tue Oct 13 17:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 14742 | 12755 | 1987 (27) | 2 | $-4732.73 | -5.1% |
| **+10¢** | 11153 | 8846 | 2307 (39) | 2 | $-4424.94 | -6.3% |
| **+15¢** | 9376 | 6905 | 2471 (57) | 2 | $-3955.85 | -6.7% |
| **+20¢** | 8342 | 5767 | 2575 (73) | 2 | $-3404.37 | -6.5% |
| **+10¢ (15¢ stop)** | 18103 | 18053 | 50 (29) | 0 | $-7044.99 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-13 17:49 | +5 | NEAR | UP | 0.62 | open |  |
| 10-13 17:48 | +10 stop | XRP | DOWN | 0.64 | 0.80 | 1.31 |
| 10-13 17:48 | +15 | XRP | DOWN | 0.64 | 0.80 | 1.31 |
| 10-13 17:48 | +10 | XRP | DOWN | 0.64 | 0.80 | 1.31 |
| 10-13 17:48 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.29 |
| 10-13 17:48 | +5 | BNB | DOWN | 0.69 | 0.78 | 0.62 |
| 10-13 17:48 | +5 | XRP | DOWN | 0.66 | 0.72 | 0.29 |
| 10-13 17:48 | +10 stop | NEAR | UP | 0.52 | 0.29 | -2.63 |
| 10-13 17:48 | +20 | NEAR | UP | 0.52 | open |  |
| 10-13 17:48 | +15 | NEAR | UP | 0.52 | open |  |
| 10-13 17:48 | +10 | NEAR | UP | 0.52 | open |  |
| 10-13 17:48 | +5 | NEAR | UP | 0.53 | 0.58 | 0.14 |
| 10-13 17:47 | +10 stop | ZEC | UP | 0.65 | 0.50 | -1.84 |
| 10-13 17:47 | +20 | ZEC | UP | 0.65 | open |  |
| 10-13 17:47 | +15 | ZEC | UP | 0.65 | open |  |
| 10-13 17:47 | +10 | ZEC | UP | 0.67 | open |  |
| 10-13 17:47 | +5 | ZEC | UP | 0.67 | open |  |
| 10-13 17:47 | +5 | BTC | DOWN | 0.62 | 0.68 | 0.27 |
| 10-13 17:46 | +10 stop | BTC | DOWN | 0.56 | 0.68 | 0.86 |
| 10-13 17:46 | +20 | BTC | DOWN | 0.56 | 0.79 | 2.00 |
| 10-13 17:46 | +15 | BTC | DOWN | 0.56 | 0.72 | 1.27 |
| 10-13 17:46 | +10 | BTC | DOWN | 0.56 | 0.68 | 0.86 |
| 10-13 17:46 | +5 | BTC | DOWN | 0.55 | 0.62 | 0.35 |
| 10-13 17:46 | +10 stop | SOL | DOWN | 0.54 | 0.72 | 1.47 |
| 10-13 17:46 | +20 | SOL | DOWN | 0.54 | 0.74 | 1.68 |
| 10-13 17:46 | +15 | SOL | DOWN | 0.54 | 0.72 | 1.47 |
| 10-13 17:46 | +10 | SOL | DOWN | 0.54 | 0.72 | 1.47 |
| 10-13 17:46 | +5 | SOL | DOWN | 0.54 | 0.62 | 0.45 |
| 10-13 17:46 | +10 stop | HYPE | DOWN | 0.55 | 0.66 | 0.76 |
| 10-13 17:46 | +20 | HYPE | DOWN | 0.55 | 0.77 | 1.89 |
| 10-13 17:46 | +15 | HYPE | DOWN | 0.55 | 0.77 | 1.89 |
| 10-13 17:46 | +10 | HYPE | DOWN | 0.55 | 0.66 | 0.76 |
| 10-13 17:46 | +5 | HYPE | DOWN | 0.55 | 0.66 | 0.76 |
| 10-13 17:46 | +10 stop | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 10-13 17:46 | +20 | ETH | DOWN | 0.66 | 0.86 | 1.75 |
| 10-13 17:46 | +15 | ETH | DOWN | 0.66 | 0.86 | 1.75 |
| 10-13 17:46 | +10 | ETH | DOWN | 0.66 | 0.79 | 1.02 |
| 10-13 17:46 | +5 | ETH | DOWN | 0.66 | 0.71 | 0.19 |
| 10-13 17:46 | +10 stop | BNB | DOWN | 0.60 | 0.71 | 0.78 |
| 10-13 17:46 | +20 | BNB | DOWN | 0.60 | 0.80 | 1.71 |
