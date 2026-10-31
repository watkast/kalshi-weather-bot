# Range-Scalp Bot

*Updated Sat Oct 31 09:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 42087 | 36716 | 5371 (55) | 6 | $-11842.37 | -4.5% |
| **+10¢** | 31374 | 25159 | 6215 (79) | 6 | $-10582.08 | -5.4% |
| **+15¢** | 26229 | 19527 | 6702 (107) | 7 | $-9693.96 | -5.9% |
| **+20¢** | 23294 | 16275 | 7019 (138) | 7 | $-8537.07 | -5.8% |
| **+10¢ (15¢ stop)** | 51316 | 51241 | 75 (41) | 2 | $-19382.29 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-31 09:52 | +10 stop | BTC | UP | 0.56 | 0.41 | -1.85 |
| 10-31 09:52 | +5 | BTC | UP | 0.55 | open |  |
| 10-31 09:52 | +10 stop | XRP | UP | 0.62 | 0.72 | 0.68 |
| 10-31 09:52 | +10 stop | DOGE | DOWN | 0.56 | open |  |
| 10-31 09:52 | +10 stop | HYPE | UP | 0.58 | 0.70 | 0.87 |
| 10-31 09:50 | +10 stop | XRP | UP | 0.71 | 0.55 | -1.93 |
| 10-31 09:50 | +10 | XRP | UP | 0.71 | open |  |
| 10-31 09:50 | +5 | XRP | UP | 0.71 | open |  |
| 10-31 09:50 | +5 | BTC | DOWN | 0.46 | 0.69 | 1.97 |
| 10-31 09:49 | +5 | SOL | DOWN | 0.63 | 0.69 | 0.28 |
| 10-31 09:49 | +10 stop | ETH | DOWN | 0.70 | 0.41 | -3.22 |
| 10-31 09:49 | +5 | BNB | DOWN | 0.62 | open |  |
| 10-31 09:48 | +10 stop | HYPE | DOWN | 0.56 | 0.33 | -2.64 |
| 10-31 09:47 | +5 | BNB | DOWN | 0.57 | 0.64 | 0.35 |
| 10-31 09:47 | +10 stop | XRP | UP | 0.62 | 0.74 | 0.89 |
| 10-31 09:47 | +20 | XRP | UP | 0.62 | open |  |
| 10-31 09:47 | +15 | XRP | UP | 0.62 | open |  |
| 10-31 09:47 | +10 | XRP | UP | 0.62 | 0.74 | 0.89 |
| 10-31 09:47 | +5 | XRP | UP | 0.62 | 0.67 | 0.17 |
| 10-31 09:46 | +10 stop | BNB | DOWN | 0.57 | open |  |
| 10-31 09:46 | +20 | BNB | DOWN | 0.57 | open |  |
| 10-31 09:46 | +15 | BNB | DOWN | 0.57 | open |  |
| 10-31 09:46 | +10 | BNB | DOWN | 0.57 | open |  |
| 10-31 09:46 | +5 | BNB | DOWN | 0.57 | 0.62 | 0.15 |
| 10-31 09:46 | +10 stop | BTC | DOWN | 0.61 | 0.46 | -1.85 |
| 10-31 09:46 | +20 | BTC | DOWN | 0.61 | open |  |
| 10-31 09:46 | +15 | BTC | DOWN | 0.61 | open |  |
| 10-31 09:46 | +10 | BTC | DOWN | 0.61 | open |  |
| 10-31 09:46 | +5 | BTC | DOWN | 0.61 | 0.69 | 0.48 |
| 10-31 09:46 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-31 09:46 | +20 | SOL | DOWN | 0.65 | open |  |
| 10-31 09:46 | +15 | SOL | DOWN | 0.65 | open |  |
| 10-31 09:46 | +10 | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 10-31 09:46 | +5 | SOL | DOWN | 0.65 | 0.73 | 0.50 |
| 10-31 09:46 | +10 stop | DOGE | DOWN | 0.67 | 0.51 | -1.94 |
| 10-31 09:46 | +20 | DOGE | DOWN | 0.67 | open |  |
| 10-31 09:46 | +15 | DOGE | DOWN | 0.67 | open |  |
| 10-31 09:46 | +10 | DOGE | DOWN | 0.68 | open |  |
| 10-31 09:46 | +5 | DOGE | DOWN | 0.68 | open |  |
| 10-31 09:45 | +10 stop | ETH | DOWN | 0.71 | 0.55 | -1.93 |
