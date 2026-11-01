# Range-Scalp Bot

*Updated Sun Nov 01 04:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 43202 | 37659 | 5543 (62) | 2 | $-12277.38 | -4.5% |
| **+10¢** | 32215 | 25809 | 6406 (84) | 4 | $-11004.27 | -5.4% |
| **+15¢** | 26956 | 20053 | 6903 (112) | 4 | $-10059.75 | -5.9% |
| **+20¢** | 23939 | 16707 | 7232 (146) | 5 | $-8885.98 | -5.9% |
| **+10¢ (15¢ stop)** | 52669 | 52586 | 83 (48) | 3 | $-19908.94 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-01 04:34 | +5 | XRP | DOWN | 0.53 | 0.59 | 0.25 |
| 11-01 04:33 | +10 stop | XRP | DOWN | 0.60 | open |  |
| 11-01 04:33 | +20 | XRP | DOWN | 0.60 | open |  |
| 11-01 04:33 | +15 | XRP | DOWN | 0.60 | open |  |
| 11-01 04:33 | +10 | XRP | DOWN | 0.60 | open |  |
| 11-01 04:33 | +5 | XRP | DOWN | 0.60 | 0.69 | 0.58 |
| 11-01 04:33 | +10 stop | BNB | DOWN | 0.70 | open |  |
| 11-01 04:33 | +20 | BNB | DOWN | 0.70 | open |  |
| 11-01 04:33 | +15 | BNB | DOWN | 0.70 | open |  |
| 11-01 04:33 | +10 | BNB | DOWN | 0.70 | open |  |
| 11-01 04:33 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 11-01 04:33 | +10 stop | BTC | DOWN | 0.59 | open |  |
| 11-01 04:33 | +20 | BTC | DOWN | 0.59 | open |  |
| 11-01 04:33 | +15 | BTC | DOWN | 0.59 | open |  |
| 11-01 04:33 | +10 | BTC | DOWN | 0.59 | open |  |
| 11-01 04:33 | +5 | BTC | DOWN | 0.60 | open |  |
| 11-01 04:32 | +5 | XRP | UP | 0.33 | 0.55 | 1.86 |
| 11-01 04:32 | +10 stop | XRP | DOWN | 0.46 | 0.73 | 2.38 |
| 11-01 04:32 | +20 | XRP | DOWN | 0.46 | 0.73 | 2.38 |
| 11-01 04:32 | +15 | XRP | DOWN | 0.46 | 0.73 | 2.38 |
| 11-01 04:32 | +10 | XRP | DOWN | 0.46 | 0.73 | 2.38 |
| 11-01 04:32 | +5 | XRP | DOWN | 0.46 | 0.55 | 0.54 |
| 11-01 04:32 | +5 | DOGE | UP | 0.57 | open |  |
| 11-01 04:31 | +10 stop | ETH | DOWN | 0.67 | 0.81 | 1.13 |
| 11-01 04:31 | +20 | ETH | DOWN | 0.65 | 0.87 | 1.96 |
| 11-01 04:31 | +15 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 11-01 04:31 | +10 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 11-01 04:31 | +5 | ETH | DOWN | 0.66 | 0.81 | 1.23 |
| 11-01 04:31 | +10 stop | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-01 04:31 | +20 | ZEC | DOWN | 0.63 | open |  |
| 11-01 04:31 | +15 | ZEC | DOWN | 0.63 | 0.80 | 1.41 |
| 11-01 04:31 | +10 | ZEC | DOWN | 0.63 | 0.74 | 0.79 |
| 11-01 04:31 | +5 | ZEC | DOWN | 0.63 | 0.72 | 0.58 |
| 11-01 04:31 | +10 stop | DOGE | UP | 0.56 | 0.36 | -2.35 |
| 11-01 04:31 | +20 | DOGE | UP | 0.56 | open |  |
| 11-01 04:31 | +15 | DOGE | UP | 0.56 | open |  |
| 11-01 04:31 | +10 | DOGE | UP | 0.56 | open |  |
| 11-01 04:31 | +5 | DOGE | UP | 0.56 | 0.61 | 0.15 |
| 11-01 04:31 | +10 stop | SOL | DOWN | 0.61 | 0.74 | 0.99 |
| 11-01 04:31 | +20 | SOL | DOWN | 0.62 | 0.91 | 2.66 |
