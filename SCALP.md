# Range-Scalp Bot

*Updated Sun Nov 15 14:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60895 | 53132 | 7763 (112) | 5 | $-16442.20 | -4.3% |
| **+10¢** | 45491 | 36390 | 9101 (150) | 5 | $-15494.14 | -5.4% |
| **+15¢** | 38095 | 28280 | 9815 (188) | 7 | $-14162.76 | -5.9% |
| **+20¢** | 33951 | 23656 | 10295 (240) | 7 | $-12444.03 | -5.8% |
| **+10¢ (15¢ stop)** | 74107 | 73956 | 151 (89) | 5 | $-27243.78 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 14:22 | +10 stop | XRP | UP | 0.56 | open |  |
| 11-15 14:22 | +20 | XRP | UP | 0.56 | open |  |
| 11-15 14:22 | +15 | XRP | UP | 0.56 | open |  |
| 11-15 14:22 | +10 | XRP | UP | 0.55 | open |  |
| 11-15 14:22 | +5 | XRP | UP | 0.54 | open |  |
| 11-15 14:22 | +10 stop | BTC | UP | 0.58 | open |  |
| 11-15 14:22 | +10 stop | BNB | UP | 0.52 | 0.63 | 0.75 |
| 11-15 14:21 | +10 stop | NEAR | UP | 0.69 | open |  |
| 11-15 14:21 | +20 | NEAR | UP | 0.69 | open |  |
| 11-15 14:21 | +15 | NEAR | UP | 0.69 | open |  |
| 11-15 14:21 | +10 | NEAR | UP | 0.69 | open |  |
| 11-15 14:21 | +5 | NEAR | UP | 0.69 | 0.77 | 0.52 |
| 11-15 14:21 | +10 stop | DOGE | DOWN | 0.57 | open |  |
| 11-15 14:21 | +5 | HYPE | DOWN | 0.70 | 0.78 | 0.52 |
| 11-15 14:21 | +10 stop | SOL | DOWN | 0.62 | open |  |
| 11-15 14:21 | +10 stop | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-15 14:21 | +20 | ETH | UP | 0.63 | open |  |
| 11-15 14:21 | +15 | ETH | UP | 0.63 | open |  |
| 11-15 14:21 | +10 | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-15 14:21 | +5 | ETH | UP | 0.63 | 0.73 | 0.69 |
| 11-15 14:20 | +5 | HYPE | DOWN | 0.57 | 0.64 | 0.37 |
| 11-15 14:20 | +10 stop | ZEC | DOWN | 0.55 | 0.67 | 0.86 |
| 11-15 14:20 | +10 stop | HYPE | DOWN | 0.56 | 0.68 | 0.86 |
| 11-15 14:20 | +10 stop | BNB | UP | 0.69 | 0.52 | -2.03 |
| 11-15 14:20 | +20 | BNB | UP | 0.69 | open |  |
| 11-15 14:20 | +15 | BNB | UP | 0.69 | open |  |
| 11-15 14:20 | +10 | BNB | UP | 0.69 | open |  |
| 11-15 14:20 | +5 | BNB | UP | 0.69 | open |  |
| 11-15 14:20 | +5 | SOL | UP | 0.58 | open |  |
| 11-15 14:19 | +10 stop | SOL | UP | 0.62 | 0.45 | -2.05 |
| 11-15 14:19 | +20 | SOL | UP | 0.62 | open |  |
| 11-15 14:19 | +15 | SOL | UP | 0.62 | open |  |
| 11-15 14:19 | +10 | SOL | UP | 0.62 | open |  |
| 11-15 14:19 | +5 | SOL | UP | 0.62 | 0.67 | 0.17 |
| 11-15 14:19 | +10 stop | BTC | UP | 0.66 | 0.47 | -2.24 |
| 11-15 14:19 | +5 | BTC | UP | 0.68 | open |  |
| 11-15 14:19 | +10 stop | DOGE | UP | 0.64 | 0.47 | -2.05 |
| 11-15 14:19 | +5 | DOGE | UP | 0.64 | open |  |
| 11-15 14:19 | +10 stop | ZEC | UP | 0.67 | 0.50 | -2.04 |
| 11-15 14:18 | +5 | ZEC | DOWN | 0.63 | 0.71 | 0.51 |
