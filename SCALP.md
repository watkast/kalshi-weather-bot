# Range-Scalp Bot

*Updated Sun Nov 15 05:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60442 | 52721 | 7721 (107) | 2 | $-16461.96 | -4.3% |
| **+10¢** | 45157 | 36110 | 9047 (143) | 3 | $-15543.69 | -5.5% |
| **+15¢** | 37822 | 28063 | 9759 (181) | 4 | $-14237.39 | -6.0% |
| **+20¢** | 33711 | 23475 | 10236 (233) | 6 | $-12529.77 | -5.9% |
| **+10¢ (15¢ stop)** | 73588 | 73445 | 143 (82) | 2 | $-27108.85 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 05:35 | +10 stop | SOL | DOWN | 0.68 | 0.79 | 0.82 |
| 11-15 05:35 | +20 | SOL | DOWN | 0.67 | open |  |
| 11-15 05:35 | +15 | SOL | DOWN | 0.63 | 0.79 | 1.31 |
| 11-15 05:35 | +10 | SOL | DOWN | 0.63 | 0.79 | 1.31 |
| 11-15 05:35 | +5 | SOL | DOWN | 0.63 | 0.79 | 1.31 |
| 11-15 05:35 | +10 stop | ZEC | DOWN | 0.58 | open |  |
| 11-15 05:35 | +10 | ZEC | DOWN | 0.58 | open |  |
| 11-15 05:33 | +5 | ZEC | DOWN | 0.67 | open |  |
| 11-15 05:33 | +5 | ETH | DOWN | 0.65 | 0.74 | 0.60 |
| 11-15 05:32 | +10 stop | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-15 05:32 | +20 | ZEC | DOWN | 0.61 | open |  |
| 11-15 05:32 | +15 | ZEC | DOWN | 0.61 | open |  |
| 11-15 05:32 | +10 | ZEC | DOWN | 0.61 | 0.71 | 0.68 |
| 11-15 05:32 | +5 | ZEC | DOWN | 0.60 | 0.67 | 0.37 |
| 11-15 05:31 | +10 stop | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 11-15 05:31 | +20 | ETH | DOWN | 0.61 | open |  |
| 11-15 05:31 | +15 | ETH | DOWN | 0.61 | open |  |
| 11-15 05:31 | +10 | ETH | DOWN | 0.61 | 0.74 | 0.99 |
| 11-15 05:31 | +5 | ETH | DOWN | 0.61 | 0.68 | 0.37 |
| 11-15 05:31 | +10 stop | BTC | DOWN | 0.66 | 0.48 | -2.14 |
| 11-15 05:31 | +20 | BTC | DOWN | 0.66 | open |  |
| 11-15 05:31 | +15 | BTC | DOWN | 0.66 | open |  |
| 11-15 05:31 | +10 | BTC | DOWN | 0.66 | open |  |
| 11-15 05:31 | +5 | BTC | DOWN | 0.66 | open |  |
| 11-15 05:31 | +10 stop | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 11-15 05:31 | +20 | XRP | DOWN | 0.64 | 0.87 | 2.05 |
| 11-15 05:31 | +15 | XRP | DOWN | 0.64 | 0.80 | 1.31 |
| 11-15 05:31 | +10 | XRP | DOWN | 0.65 | 0.77 | 0.91 |
| 11-15 05:31 | +5 | XRP | DOWN | 0.65 | 0.70 | 0.19 |
| 11-15 05:31 | +10 stop | BNB | DOWN | 0.69 | open |  |
| 11-15 05:31 | +20 | BNB | DOWN | 0.69 | open |  |
| 11-15 05:31 | +15 | BNB | DOWN | 0.69 | open |  |
| 11-15 05:31 | +10 | BNB | DOWN | 0.69 | open |  |
| 11-15 05:31 | +5 | BNB | DOWN | 0.69 | 0.75 | 0.31 |
| 11-15 05:31 | +10 stop | NEAR | DOWN | 0.66 | 0.78 | 0.91 |
| 11-15 05:31 | +20 | NEAR | DOWN | 0.66 | open |  |
| 11-15 05:31 | +15 | NEAR | DOWN | 0.66 | 0.83 | 1.44 |
| 11-15 05:31 | +10 | NEAR | DOWN | 0.66 | 0.78 | 0.91 |
| 11-15 05:31 | +5 | NEAR | DOWN | 0.66 | 0.73 | 0.40 |
| 11-15 05:28 | +10 | HYPE | UP | 0.69 | 0.96 | 2.56 |
