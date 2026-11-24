# Range-Scalp Bot

*Updated Tue Nov 24 19:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 70945 | 61927 | 9018 (155) | 1 | $-18882.37 | -4.2% |
| **+10¢** | 52918 | 42389 | 10529 (201) | 4 | $-17459.95 | -5.2% |
| **+15¢** | 44318 | 32976 | 11342 (258) | 5 | $-15556.77 | -5.6% |
| **+20¢** | 39459 | 27518 | 11941 (324) | 4 | $-13926.87 | -5.6% |
| **+10¢ (15¢ stop)** | 86366 | 86165 | 201 (121) | 0 | $-31728.19 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-24 19:13 | +10 stop | SOL | UP | 0.68 | 0.85 | 1.45 |
| 11-24 19:13 | +10 stop | HYPE | UP | 0.67 | 0.49 | -2.14 |
| 11-24 19:13 | +10 | HYPE | UP | 0.67 | 0.97 | 2.79 |
| 11-24 19:12 | +10 stop | ZEC | UP | 0.43 | 0.56 | 0.94 |
| 11-24 19:12 | +5 | HYPE | UP | 0.61 | 0.97 | 3.38 |
| 11-24 19:12 | +5 | ZEC | UP | 0.47 | 0.56 | 0.54 |
| 11-24 19:12 | +10 stop | DOGE | UP | 0.69 | 0.84 | 1.24 |
| 11-24 19:12 | +5 | DOGE | UP | 0.69 | 0.74 | 0.21 |
| 11-24 19:12 | +10 stop | SOL | DOWN | 0.61 | 0.43 | -2.15 |
| 11-24 19:12 | +20 | SOL | DOWN | 0.61 | open |  |
| 11-24 19:12 | +15 | SOL | DOWN | 0.59 | open |  |
| 11-24 19:12 | +10 | SOL | DOWN | 0.59 | open |  |
| 11-24 19:12 | +5 | SOL | DOWN | 0.59 | open |  |
| 11-24 19:12 | +10 stop | ZEC | DOWN | 0.61 | 0.43 | -2.15 |
| 11-24 19:12 | +20 | ZEC | DOWN | 0.61 | open |  |
| 11-24 19:12 | +15 | ZEC | DOWN | 0.61 | open |  |
| 11-24 19:12 | +10 | ZEC | DOWN | 0.61 | open |  |
| 11-24 19:12 | +5 | ZEC | DOWN | 0.62 | 0.67 | 0.20 |
| 11-24 19:12 | +10 stop | HYPE | DOWN | 0.49 | 0.33 | -1.95 |
| 11-24 19:11 | +10 stop | DOGE | DOWN | 0.52 | 0.34 | -2.14 |
| 11-24 19:11 | +20 | DOGE | DOWN | 0.52 | open |  |
| 11-24 19:11 | +15 | DOGE | DOWN | 0.48 | open |  |
| 11-24 19:11 | +10 | DOGE | DOWN | 0.47 | open |  |
| 11-24 19:11 | +5 | DOGE | DOWN | 0.47 | 0.56 | 0.54 |
| 11-24 19:10 | +10 stop | BTC | DOWN | 0.52 | 0.29 | -2.63 |
| 11-24 19:10 | +10 stop | BNB | DOWN | 0.60 | 0.42 | -2.15 |
| 11-24 19:10 | +10 | BNB | DOWN | 0.56 | open |  |
| 11-24 19:10 | +10 stop | ETH | DOWN | 0.60 | 0.74 | 1.09 |
| 11-24 19:09 | +5 | BNB | UP | 0.59 | 0.72 | 0.98 |
| 11-24 19:09 | +10 stop | BTC | UP | 0.55 | 0.36 | -2.25 |
| 11-24 19:09 | +10 stop | BNB | DOWN | 0.53 | 0.64 | 0.75 |
| 11-24 19:09 | +15 | BNB | DOWN | 0.54 | open |  |
| 11-24 19:09 | +10 | BNB | DOWN | 0.54 | 0.64 | 0.65 |
| 11-24 19:09 | +5 | BNB | DOWN | 0.54 | 0.60 | 0.25 |
| 11-24 19:09 | +10 stop | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-24 19:09 | +10 | ZEC | DOWN | 0.70 | 0.83 | 1.05 |
| 11-24 19:09 | +5 | ZEC | DOWN | 0.70 | 0.78 | 0.52 |
| 11-24 19:08 | +10 stop | DOGE | DOWN | 0.61 | 0.83 | 1.93 |
| 11-24 19:08 | +10 | DOGE | DOWN | 0.61 | 0.83 | 1.93 |
| 11-24 19:08 | +10 stop | ETH | DOWN | 0.71 | 0.53 | -2.13 |
