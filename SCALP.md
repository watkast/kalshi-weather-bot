# Range-Scalp Bot

*Updated Wed Oct 28 17:02 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38225 | 33350 | 4875 (46) | 7 | $-10796.41 | -4.5% |
| **+10¢** | 28514 | 22881 | 5633 (68) | 7 | $-9596.73 | -5.3% |
| **+15¢** | 23859 | 17812 | 6047 (93) | 7 | $-8529.47 | -5.7% |
| **+20¢** | 21166 | 14833 | 6333 (118) | 7 | $-7489.25 | -5.6% |
| **+10¢ (15¢ stop)** | 46785 | 46718 | 67 (35) | 7 | $-17756.89 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-28 17:02 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 10-28 17:02 | +20 | BNB | DOWN | 0.65 | open |  |
| 10-28 17:02 | +15 | BNB | DOWN | 0.67 | open |  |
| 10-28 17:02 | +10 | BNB | DOWN | 0.67 | open |  |
| 10-28 17:02 | +5 | BNB | DOWN | 0.68 | open |  |
| 10-28 17:02 | +10 stop | DOGE | DOWN | 0.64 | open |  |
| 10-28 17:02 | +20 | DOGE | DOWN | 0.64 | open |  |
| 10-28 17:02 | +15 | DOGE | DOWN | 0.64 | open |  |
| 10-28 17:02 | +10 | DOGE | DOWN | 0.64 | open |  |
| 10-28 17:02 | +5 | DOGE | DOWN | 0.64 | open |  |
| 10-28 17:01 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 10-28 17:01 | +20 | NEAR | DOWN | 0.69 | open |  |
| 10-28 17:01 | +15 | NEAR | DOWN | 0.69 | open |  |
| 10-28 17:01 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-28 17:01 | +5 | NEAR | DOWN | 0.69 | open |  |
| 10-28 17:01 | +10 stop | XRP | DOWN | 0.62 | open |  |
| 10-28 17:01 | +20 | XRP | DOWN | 0.61 | open |  |
| 10-28 17:01 | +15 | XRP | DOWN | 0.61 | open |  |
| 10-28 17:01 | +10 | XRP | DOWN | 0.61 | open |  |
| 10-28 17:01 | +5 | XRP | DOWN | 0.61 | open |  |
| 10-28 17:01 | +10 stop | SOL | DOWN | 0.63 | open |  |
| 10-28 17:01 | +20 | SOL | DOWN | 0.63 | open |  |
| 10-28 17:01 | +15 | SOL | DOWN | 0.63 | open |  |
| 10-28 17:01 | +10 | SOL | DOWN | 0.63 | open |  |
| 10-28 17:01 | +5 | SOL | DOWN | 0.63 | open |  |
| 10-28 17:00 | +10 stop | ETH | DOWN | 0.71 | open |  |
| 10-28 17:00 | +20 | ETH | DOWN | 0.71 | open |  |
| 10-28 17:00 | +15 | ETH | DOWN | 0.71 | open |  |
| 10-28 17:00 | +10 | ETH | DOWN | 0.71 | open |  |
| 10-28 17:00 | +5 | ETH | DOWN | 0.71 | open |  |
| 10-28 17:00 | +10 stop | ZEC | DOWN | 0.70 | open |  |
| 10-28 17:00 | +20 | ZEC | DOWN | 0.70 | open |  |
| 10-28 17:00 | +15 | ZEC | DOWN | 0.71 | open |  |
| 10-28 17:00 | +10 | ZEC | DOWN | 0.71 | open |  |
| 10-28 17:00 | +5 | ZEC | DOWN | 0.71 | open |  |
| 10-28 16:53 | +5 | XRP | UP | 0.70 | 0.78 | 0.52 |
| 10-28 16:52 | +10 stop | BTC | DOWN | 0.55 | 0.38 | -2.05 |
| 10-28 16:52 | +20 | BTC | DOWN | 0.55 | yes | -5.68 |
| 10-28 16:52 | +15 | BTC | DOWN | 0.56 | yes | -5.78 |
| 10-28 16:52 | +10 | BTC | DOWN | 0.56 | yes | -5.78 |
