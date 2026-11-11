# Range-Scalp Bot

*Updated Wed Nov 11 22:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56293 | 49090 | 7203 (95) | 2 | $-15399.67 | -4.3% |
| **+10¢** | 42066 | 33660 | 8406 (125) | 2 | $-14368.77 | -5.4% |
| **+15¢** | 35275 | 26217 | 9058 (159) | 2 | $-13048.63 | -5.9% |
| **+20¢** | 31427 | 21923 | 9504 (209) | 2 | $-11404.56 | -5.8% |
| **+10¢ (15¢ stop)** | 68606 | 68485 | 121 (73) | 2 | $-25299.76 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 22:31 | +10 stop | ZEC | UP | 0.50 | open |  |
| 11-11 22:31 | +20 | ZEC | UP | 0.50 | open |  |
| 11-11 22:31 | +15 | ZEC | UP | 0.50 | open |  |
| 11-11 22:31 | +10 | ZEC | UP | 0.50 | open |  |
| 11-11 22:31 | +5 | ZEC | UP | 0.50 | open |  |
| 11-11 22:31 | +10 stop | HYPE | UP | 0.60 | open |  |
| 11-11 22:31 | +20 | HYPE | UP | 0.61 | open |  |
| 11-11 22:31 | +15 | HYPE | UP | 0.61 | open |  |
| 11-11 22:31 | +10 | HYPE | UP | 0.61 | open |  |
| 11-11 22:31 | +5 | HYPE | UP | 0.61 | open |  |
| 11-11 22:26 | +10 stop | ZEC | DOWN | 0.70 | 0.84 | 1.15 |
| 11-11 22:26 | +20 | ZEC | DOWN | 0.70 | 0.97 | 2.56 |
| 11-11 22:26 | +15 | ZEC | DOWN | 0.70 | 0.97 | 2.56 |
| 11-11 22:26 | +10 | ZEC | DOWN | 0.70 | 0.84 | 1.15 |
| 11-11 22:26 | +5 | ZEC | DOWN | 0.70 | 0.77 | 0.42 |
| 11-11 22:24 | +5 | DOGE | DOWN | 0.61 | 0.73 | 0.89 |
| 11-11 22:24 | +10 stop | DOGE | DOWN | 0.60 | 0.73 | 0.99 |
| 11-11 22:24 | +10 stop | XRP | DOWN | 0.61 | 0.74 | 0.99 |
| 11-11 22:24 | +10 | SOL | UP | 0.56 | no | -5.78 |
| 11-11 22:24 | +5 | SOL | UP | 0.56 | no | -5.78 |
| 11-11 22:24 | +10 stop | NEAR | DOWN | 0.71 | 0.86 | 1.29 |
| 11-11 22:24 | +10 stop | BNB | DOWN | 0.55 | 0.74 | 1.58 |
| 11-11 22:24 | +10 stop | SOL | UP | 0.56 | 0.39 | -2.05 |
| 11-11 22:24 | +20 | SOL | UP | 0.56 | no | -5.78 |
| 11-11 22:24 | +15 | SOL | UP | 0.54 | no | -5.58 |
| 11-11 22:24 | +10 | SOL | UP | 0.54 | 0.64 | 0.65 |
| 11-11 22:24 | +5 | SOL | UP | 0.56 | 0.64 | 0.45 |
| 11-11 22:21 | +10 stop | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-11 22:21 | +10 stop | XRP | DOWN | 0.61 | 0.72 | 0.78 |
| 11-11 22:21 | +10 stop | NEAR | UP | 0.58 | 0.33 | -2.84 |
| 11-11 22:21 | +10 | NEAR | UP | 0.58 | no | -5.98 |
| 11-11 22:21 | +5 | NEAR | UP | 0.58 | no | -5.98 |
| 11-11 22:20 | +10 stop | BNB | UP | 0.68 | 0.44 | -2.75 |
| 11-11 22:19 | +5 | BTC | UP | 0.62 | no | -6.37 |
| 11-11 22:19 | +5 | XRP | UP | 0.66 | no | -6.76 |
| 11-11 22:18 | +10 stop | XRP | UP | 0.67 | 0.47 | -2.34 |
| 11-11 22:18 | +20 | XRP | UP | 0.67 | no | -6.86 |
| 11-11 22:18 | +15 | XRP | UP | 0.67 | no | -6.86 |
| 11-11 22:18 | +10 | XRP | UP | 0.67 | no | -6.86 |
| 11-11 22:18 | +5 | XRP | UP | 0.67 | 0.72 | 0.19 |
