# Range-Scalp Bot

*Updated Wed Nov 11 13:48 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55897 | 48746 | 7151 (94) | 2 | $-15278.13 | -4.3% |
| **+10¢** | 41765 | 33425 | 8340 (124) | 5 | $-14214.13 | -5.4% |
| **+15¢** | 35023 | 26026 | 8997 (158) | 6 | $-12977.53 | -5.9% |
| **+20¢** | 31193 | 21754 | 9439 (208) | 6 | $-11355.32 | -5.8% |
| **+10¢ (15¢ stop)** | 68085 | 67964 | 121 (73) | 5 | $-25028.58 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 13:47 | +5 | ETH | UP | 0.65 | open |  |
| 11-11 13:46 | +10 stop | BNB | UP | 0.71 | open |  |
| 11-11 13:46 | +20 | BNB | UP | 0.71 | open |  |
| 11-11 13:46 | +15 | BNB | UP | 0.71 | open |  |
| 11-11 13:46 | +10 | BNB | UP | 0.71 | open |  |
| 11-11 13:46 | +5 | BNB | UP | 0.71 | 0.76 | 0.22 |
| 11-11 13:46 | +10 stop | ETH | UP | 0.55 | open |  |
| 11-11 13:46 | +20 | ETH | UP | 0.55 | open |  |
| 11-11 13:46 | +15 | ETH | UP | 0.56 | open |  |
| 11-11 13:46 | +10 | ETH | UP | 0.56 | open |  |
| 11-11 13:46 | +5 | ETH | UP | 0.56 | 0.62 | 0.25 |
| 11-11 13:46 | +10 stop | SOL | UP | 0.63 | open |  |
| 11-11 13:46 | +20 | SOL | UP | 0.63 | open |  |
| 11-11 13:46 | +15 | SOL | UP | 0.64 | open |  |
| 11-11 13:46 | +10 | SOL | UP | 0.64 | open |  |
| 11-11 13:46 | +5 | SOL | UP | 0.64 | 0.70 | 0.28 |
| 11-11 13:46 | +10 stop | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-11 13:46 | +20 | NEAR | UP | 0.70 | open |  |
| 11-11 13:46 | +15 | NEAR | UP | 0.70 | open |  |
| 11-11 13:46 | +10 | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-11 13:46 | +5 | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-11 13:46 | +10 stop | ZEC | UP | 0.67 | open |  |
| 11-11 13:46 | +20 | ZEC | UP | 0.67 | open |  |
| 11-11 13:46 | +15 | ZEC | UP | 0.67 | open |  |
| 11-11 13:46 | +10 | ZEC | UP | 0.67 | open |  |
| 11-11 13:46 | +5 | ZEC | UP | 0.67 | 0.74 | 0.40 |
| 11-11 13:46 | +10 stop | BTC | UP | 0.59 | open |  |
| 11-11 13:46 | +20 | BTC | UP | 0.59 | open |  |
| 11-11 13:46 | +15 | BTC | UP | 0.59 | open |  |
| 11-11 13:46 | +10 | BTC | UP | 0.59 | open |  |
| 11-11 13:46 | +5 | BTC | UP | 0.59 | open |  |
| 11-11 13:42 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-11 13:42 | +20 | SOL | DOWN | 0.64 | 0.94 | 2.80 |
| 11-11 13:42 | +15 | SOL | DOWN | 0.64 | 0.82 | 1.52 |
| 11-11 13:42 | +10 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-11 13:42 | +5 | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 11-11 13:36 | +10 stop | BNB | DOWN | 0.71 | 0.83 | 0.95 |
| 11-11 13:34 | +5 | BNB | UP | 0.60 | no | -6.17 |
| 11-11 13:34 | +10 stop | HYPE | DOWN | 0.69 | 0.82 | 1.04 |
| 11-11 13:34 | +20 | HYPE | DOWN | 0.68 | 0.90 | 1.97 |
