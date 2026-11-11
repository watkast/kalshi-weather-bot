# Range-Scalp Bot

*Updated Wed Nov 11 11:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55719 | 48589 | 7130 (94) | 1 | $-15241.09 | -4.3% |
| **+10¢** | 41636 | 33320 | 8316 (124) | 2 | $-14179.48 | -5.4% |
| **+15¢** | 34909 | 25939 | 8970 (158) | 3 | $-12950.33 | -5.9% |
| **+20¢** | 31091 | 21682 | 9409 (208) | 3 | $-11321.50 | -5.8% |
| **+10¢ (15¢ stop)** | 67874 | 67753 | 121 (73) | 0 | $-24966.49 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 11:13 | +10 stop | SOL | DOWN | 0.39 | 0.57 | 1.45 |
| 11-11 11:13 | +20 | SOL | DOWN | 0.39 | open |  |
| 11-11 11:13 | +15 | SOL | DOWN | 0.39 | 0.57 | 1.45 |
| 11-11 11:11 | +10 stop | ZEC | UP | 0.62 | 0.78 | 1.28 |
| 11-11 11:10 | +10 stop | XRP | DOWN | 0.59 | 0.73 | 1.09 |
| 11-11 11:10 | +20 | XRP | DOWN | 0.59 | 0.83 | 2.13 |
| 11-11 11:10 | +10 stop | ETH | DOWN | 0.61 | 0.46 | -1.85 |
| 11-11 11:09 | +10 stop | ETH | UP | 0.31 | 0.55 | 2.07 |
| 11-11 11:09 | +10 stop | ZEC | UP | 0.48 | 0.58 | 0.64 |
| 11-11 11:09 | +10 stop | DOGE | DOWN | 0.70 | 0.87 | 1.47 |
| 11-11 11:09 | +10 stop | XRP | DOWN | 0.55 | 0.65 | 0.66 |
| 11-11 11:09 | +20 | XRP | DOWN | 0.55 | 0.75 | 1.68 |
| 11-11 11:07 | +10 stop | ZEC | UP | 0.46 | 0.66 | 1.66 |
| 11-11 11:07 | +10 stop | ETH | DOWN | 0.62 | 0.43 | -2.25 |
| 11-11 11:06 | +10 stop | ZEC | DOWN | 0.59 | 0.41 | -2.14 |
| 11-11 11:06 | +10 stop | SOL | DOWN | 0.61 | 0.73 | 0.84 |
| 11-11 11:06 | +10 stop | XRP | DOWN | 0.59 | 0.70 | 0.78 |
| 11-11 11:05 | +10 stop | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-11 11:05 | +10 | BTC | DOWN | 0.67 | 0.79 | 0.92 |
| 11-11 11:05 | +5 | HYPE | UP | 0.69 | 0.78 | 0.62 |
| 11-11 11:05 | +5 | BTC | DOWN | 0.64 | 0.79 | 1.21 |
| 11-11 11:04 | +5 | BTC | DOWN | 0.58 | 0.63 | 0.15 |
| 11-11 11:04 | +10 stop | SOL | DOWN | 0.50 | 0.64 | 1.05 |
| 11-11 11:04 | +10 stop | ZEC | DOWN | 0.62 | 0.44 | -2.15 |
| 11-11 11:04 | +5 | ZEC | DOWN | 0.62 | open |  |
| 11-11 11:03 | +10 stop | XRP | UP | 0.67 | 0.42 | -2.84 |
| 11-11 11:03 | +10 stop | DOGE | DOWN | 0.66 | 0.77 | 0.81 |
| 11-11 11:03 | +5 | NEAR | UP | 0.59 | 0.76 | 1.40 |
| 11-11 11:03 | +10 stop | HYPE | UP | 0.64 | 0.78 | 1.10 |
| 11-11 11:03 | +5 | HYPE | UP | 0.64 | 0.69 | 0.18 |
| 11-11 11:02 | +10 stop | BTC | UP | 0.48 | 0.33 | -1.84 |
| 11-11 11:02 | +10 stop | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-11 11:02 | +10 stop | DOGE | UP | 0.67 | 0.48 | -2.24 |
| 11-11 11:02 | +20 | DOGE | UP | 0.67 | 0.89 | 1.97 |
| 11-11 11:02 | +15 | DOGE | UP | 0.68 | 0.89 | 1.87 |
| 11-11 11:02 | +10 | DOGE | UP | 0.66 | 0.89 | 2.07 |
| 11-11 11:02 | +5 | DOGE | UP | 0.66 | 0.89 | 2.07 |
| 11-11 11:02 | +10 stop | SOL | UP | 0.64 | 0.46 | -2.15 |
| 11-11 11:02 | +10 | SOL | UP | 0.64 | 0.87 | 2.05 |
| 11-11 11:02 | +5 | SOL | UP | 0.64 | 0.87 | 2.05 |
