# Range-Scalp Bot

*Updated Fri Oct 23 02:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 29607 | 25765 | 3842 (39) | 5 | $-8777.23 | -4.7% |
| **+10¢** | 22204 | 17757 | 4447 (55) | 8 | $-7906.29 | -5.7% |
| **+15¢** | 18591 | 13817 | 4774 (78) | 8 | $-7088.40 | -6.1% |
| **+20¢** | 16455 | 11452 | 5003 (100) | 8 | $-6417.41 | -6.2% |
| **+10¢ (15¢ stop)** | 36356 | 36297 | 59 (32) | 7 | $-13731.37 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 02:04 | +5 | DOGE | DOWN | 0.68 | 0.74 | 0.30 |
| 10-23 02:02 | +10 stop | DOGE | DOWN | 0.65 | open |  |
| 10-23 02:02 | +20 | DOGE | DOWN | 0.65 | open |  |
| 10-23 02:02 | +15 | DOGE | DOWN | 0.65 | open |  |
| 10-23 02:02 | +10 | DOGE | DOWN | 0.65 | open |  |
| 10-23 02:02 | +5 | DOGE | DOWN | 0.65 | 0.70 | 0.19 |
| 10-23 02:02 | +10 stop | ETH | DOWN | 0.54 | open |  |
| 10-23 02:02 | +10 stop | NEAR | DOWN | 0.68 | open |  |
| 10-23 02:02 | +20 | NEAR | DOWN | 0.68 | open |  |
| 10-23 02:02 | +15 | NEAR | DOWN | 0.68 | open |  |
| 10-23 02:02 | +10 | NEAR | DOWN | 0.69 | open |  |
| 10-23 02:02 | +5 | NEAR | DOWN | 0.70 | open |  |
| 10-23 02:01 | +5 | XRP | DOWN | 0.68 | open |  |
| 10-23 02:01 | +10 stop | SOL | DOWN | 0.70 | open |  |
| 10-23 02:01 | +20 | SOL | DOWN | 0.70 | open |  |
| 10-23 02:01 | +15 | SOL | DOWN | 0.70 | open |  |
| 10-23 02:01 | +10 | SOL | DOWN | 0.70 | open |  |
| 10-23 02:01 | +5 | SOL | DOWN | 0.70 | open |  |
| 10-23 02:01 | +10 stop | HYPE | DOWN | 0.66 | 0.77 | 0.77 |
| 10-23 02:01 | +20 | HYPE | DOWN | 0.66 | open |  |
| 10-23 02:01 | +15 | HYPE | DOWN | 0.66 | open |  |
| 10-23 02:01 | +10 | HYPE | DOWN | 0.67 | open |  |
| 10-23 02:01 | +5 | HYPE | DOWN | 0.67 | 0.77 | 0.67 |
| 10-23 02:00 | +10 stop | XRP | DOWN | 0.64 | open |  |
| 10-23 02:00 | +20 | XRP | DOWN | 0.64 | open |  |
| 10-23 02:00 | +15 | XRP | DOWN | 0.64 | open |  |
| 10-23 02:00 | +10 | XRP | DOWN | 0.63 | open |  |
| 10-23 02:00 | +5 | XRP | DOWN | 0.63 | 0.68 | 0.17 |
| 10-23 02:00 | +10 stop | BNB | DOWN | 0.67 | open |  |
| 10-23 02:00 | +20 | BNB | DOWN | 0.67 | open |  |
| 10-23 02:00 | +15 | BNB | DOWN | 0.67 | open |  |
| 10-23 02:00 | +10 | BNB | DOWN | 0.67 | open |  |
| 10-23 02:00 | +5 | BNB | DOWN | 0.67 | open |  |
| 10-23 02:00 | +10 stop | BTC | DOWN | 0.65 | open |  |
| 10-23 02:00 | +20 | BTC | DOWN | 0.65 | open |  |
| 10-23 02:00 | +15 | BTC | DOWN | 0.65 | open |  |
| 10-23 02:00 | +10 | BTC | DOWN | 0.65 | open |  |
| 10-23 02:00 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-23 02:00 | +10 stop | ETH | DOWN | 0.64 | 0.49 | -1.85 |
| 10-23 02:00 | +20 | ETH | DOWN | 0.64 | open |  |
