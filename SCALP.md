# Range-Scalp Bot

*Updated Sun Nov 08 08:56 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 52227 | 45535 | 6692 (82) | 5 | $-14487.55 | -4.4% |
| **+10¢** | 38982 | 31181 | 7801 (107) | 5 | $-13486.07 | -5.5% |
| **+15¢** | 32653 | 24246 | 8407 (137) | 5 | $-12356.66 | -6.0% |
| **+20¢** | 29042 | 20230 | 8812 (181) | 5 | $-10884.40 | -6.0% |
| **+10¢ (15¢ stop)** | 63577 | 63472 | 105 (62) | 1 | $-23487.11 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-08 08:55 | +10 stop | ZEC | DOWN | 0.71 | open |  |
| 11-08 08:55 | +10 | ZEC | DOWN | 0.71 | open |  |
| 11-08 08:55 | +5 | ZEC | DOWN | 0.71 | open |  |
| 11-08 08:55 | +10 stop | ETH | UP | 0.61 | 0.74 | 0.99 |
| 11-08 08:53 | +10 stop | SOL | UP | 0.65 | 0.46 | -2.24 |
| 11-08 08:53 | +10 stop | BTC | UP | 0.53 | 0.67 | 1.06 |
| 11-08 08:52 | +10 stop | BNB | UP | 0.69 | 0.87 | 1.57 |
| 11-08 08:51 | +10 stop | ETH | UP | 0.63 | 0.79 | 1.31 |
| 11-08 08:51 | +10 stop | SOL | DOWN | 0.60 | 0.41 | -2.24 |
| 11-08 08:51 | +15 | SOL | DOWN | 0.60 | open |  |
| 11-08 08:51 | +10 | SOL | DOWN | 0.60 | open |  |
| 11-08 08:51 | +5 | SOL | DOWN | 0.60 | open |  |
| 11-08 08:51 | +10 stop | BNB | DOWN | 0.60 | 0.43 | -2.02 |
| 11-08 08:51 | +15 | BNB | DOWN | 0.60 | open |  |
| 11-08 08:51 | +10 | BNB | DOWN | 0.60 | open |  |
| 11-08 08:51 | +5 | BNB | DOWN | 0.60 | open |  |
| 11-08 08:50 | +10 stop | BTC | DOWN | 0.61 | 0.35 | -2.93 |
| 11-08 08:48 | +5 | ETH | DOWN | 0.68 | open |  |
| 11-08 08:47 | +10 stop | BTC | DOWN | 0.69 | 0.54 | -1.83 |
| 11-08 08:47 | +20 | BTC | DOWN | 0.69 | open |  |
| 11-08 08:47 | +15 | BTC | DOWN | 0.69 | open |  |
| 11-08 08:47 | +10 | BTC | DOWN | 0.69 | open |  |
| 11-08 08:47 | +5 | BTC | DOWN | 0.69 | open |  |
| 11-08 08:47 | +5 | BNB | DOWN | 0.63 | 0.68 | 0.17 |
| 11-08 08:46 | +5 | SOL | DOWN | 0.66 | 0.73 | 0.40 |
| 11-08 08:46 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-08 08:46 | +20 | ZEC | DOWN | 0.71 | open |  |
| 11-08 08:46 | +15 | ZEC | DOWN | 0.71 | open |  |
| 11-08 08:46 | +10 | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-08 08:46 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-08 08:45 | +10 stop | ETH | DOWN | 0.62 | 0.38 | -2.74 |
| 11-08 08:45 | +20 | ETH | DOWN | 0.62 | open |  |
| 11-08 08:45 | +15 | ETH | DOWN | 0.62 | open |  |
| 11-08 08:45 | +10 | ETH | DOWN | 0.62 | open |  |
| 11-08 08:45 | +5 | ETH | DOWN | 0.62 | 0.67 | 0.17 |
| 11-08 08:45 | +10 stop | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 11-08 08:45 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 11-08 08:45 | +15 | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 11-08 08:45 | +10 | NEAR | DOWN | 0.67 | 0.82 | 1.23 |
| 11-08 08:45 | +5 | NEAR | DOWN | 0.67 | 0.73 | 0.30 |
