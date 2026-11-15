# Range-Scalp Bot

*Updated Sun Nov 15 00:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60032 | 52364 | 7668 (107) | 7 | $-16352.30 | -4.3% |
| **+10¢** | 44853 | 35870 | 8983 (143) | 7 | $-15429.63 | -5.5% |
| **+15¢** | 37582 | 27894 | 9688 (181) | 7 | $-14077.44 | -6.0% |
| **+20¢** | 33485 | 23321 | 10164 (233) | 7 | $-12413.51 | -5.9% |
| **+10¢ (15¢ stop)** | 73084 | 72941 | 143 (82) | 7 | $-26876.28 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 00:02 | +5 | BNB | DOWN | 0.60 | open |  |
| 11-15 00:02 | +5 | SOL | DOWN | 0.62 | open |  |
| 11-15 00:01 | +10 stop | ZEC | DOWN | 0.60 | open |  |
| 11-15 00:01 | +20 | ZEC | DOWN | 0.60 | open |  |
| 11-15 00:01 | +15 | ZEC | DOWN | 0.61 | open |  |
| 11-15 00:01 | +10 | ZEC | DOWN | 0.60 | open |  |
| 11-15 00:01 | +5 | ZEC | DOWN | 0.59 | open |  |
| 11-15 00:01 | +10 stop | BNB | DOWN | 0.58 | open |  |
| 11-15 00:01 | +20 | BNB | DOWN | 0.58 | open |  |
| 11-15 00:01 | +15 | BNB | DOWN | 0.58 | open |  |
| 11-15 00:01 | +10 | BNB | DOWN | 0.57 | open |  |
| 11-15 00:01 | +5 | BNB | DOWN | 0.57 | 0.64 | 0.35 |
| 11-15 00:01 | +10 stop | DOGE | DOWN | 0.60 | open |  |
| 11-15 00:01 | +20 | DOGE | DOWN | 0.60 | open |  |
| 11-15 00:01 | +15 | DOGE | DOWN | 0.60 | open |  |
| 11-15 00:01 | +10 | DOGE | DOWN | 0.61 | open |  |
| 11-15 00:01 | +5 | DOGE | DOWN | 0.61 | open |  |
| 11-15 00:01 | +10 stop | BTC | DOWN | 0.62 | open |  |
| 11-15 00:01 | +20 | BTC | DOWN | 0.62 | open |  |
| 11-15 00:01 | +15 | BTC | DOWN | 0.63 | open |  |
| 11-15 00:01 | +10 | BTC | DOWN | 0.63 | open |  |
| 11-15 00:01 | +5 | BTC | DOWN | 0.64 | open |  |
| 11-15 00:01 | +10 stop | SOL | DOWN | 0.63 | open |  |
| 11-15 00:01 | +20 | SOL | DOWN | 0.63 | open |  |
| 11-15 00:01 | +15 | SOL | DOWN | 0.63 | open |  |
| 11-15 00:01 | +10 | SOL | DOWN | 0.63 | open |  |
| 11-15 00:01 | +5 | SOL | DOWN | 0.63 | 0.68 | 0.18 |
| 11-15 00:01 | +10 stop | ETH | DOWN | 0.65 | open |  |
| 11-15 00:01 | +20 | ETH | DOWN | 0.65 | open |  |
| 11-15 00:01 | +15 | ETH | DOWN | 0.65 | open |  |
| 11-15 00:01 | +10 | ETH | DOWN | 0.65 | open |  |
| 11-15 00:01 | +5 | ETH | DOWN | 0.65 | open |  |
| 11-15 00:01 | +10 stop | HYPE | DOWN | 0.56 | open |  |
| 11-15 00:01 | +20 | HYPE | DOWN | 0.56 | open |  |
| 11-15 00:01 | +15 | HYPE | DOWN | 0.56 | open |  |
| 11-15 00:01 | +10 | HYPE | DOWN | 0.56 | open |  |
| 11-15 00:01 | +5 | HYPE | DOWN | 0.56 | open |  |
| 11-14 23:44 | +10 stop | ETH | DOWN | 0.43 | 0.62 | 1.55 |
| 11-14 23:44 | +20 | ETH | DOWN | 0.47 | yes | -4.88 |
| 11-14 23:44 | +15 | ETH | DOWN | 0.47 | 0.62 | 1.15 |
