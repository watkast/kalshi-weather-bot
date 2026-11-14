# Range-Scalp Bot

*Updated Sat Nov 14 09:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59249 | 51697 | 7552 (107) | 0 | $-15997.62 | -4.3% |
| **+10¢** | 44259 | 35420 | 8839 (140) | 6 | $-15030.38 | -5.4% |
| **+15¢** | 37089 | 27558 | 9531 (176) | 6 | $-13666.62 | -5.9% |
| **+20¢** | 33039 | 23033 | 10006 (228) | 6 | $-12062.78 | -5.8% |
| **+10¢ (15¢ stop)** | 72094 | 71952 | 142 (82) | 6 | $-26503.29 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 09:15 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 11-14 09:15 | +20 | NEAR | DOWN | 0.69 | open |  |
| 11-14 09:15 | +15 | NEAR | DOWN | 0.69 | open |  |
| 11-14 09:15 | +10 | NEAR | DOWN | 0.69 | open |  |
| 11-14 09:15 | +5 | NEAR | DOWN | 0.69 | 0.77 | 0.52 |
| 11-14 09:15 | +10 stop | BTC | DOWN | 0.70 | open |  |
| 11-14 09:15 | +20 | BTC | DOWN | 0.70 | open |  |
| 11-14 09:15 | +15 | BTC | DOWN | 0.70 | open |  |
| 11-14 09:15 | +10 | BTC | DOWN | 0.70 | open |  |
| 11-14 09:15 | +5 | BTC | DOWN | 0.70 | 0.76 | 0.32 |
| 11-14 09:15 | +10 stop | BNB | DOWN | 0.69 | open |  |
| 11-14 09:15 | +20 | BNB | DOWN | 0.69 | open |  |
| 11-14 09:15 | +15 | BNB | DOWN | 0.69 | open |  |
| 11-14 09:15 | +10 | BNB | DOWN | 0.69 | open |  |
| 11-14 09:15 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 11-14 09:15 | +10 stop | SOL | DOWN | 0.71 | open |  |
| 11-14 09:15 | +20 | SOL | DOWN | 0.71 | open |  |
| 11-14 09:15 | +15 | SOL | DOWN | 0.71 | open |  |
| 11-14 09:15 | +10 | SOL | DOWN | 0.71 | open |  |
| 11-14 09:15 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
| 11-14 09:15 | +10 stop | ETH | DOWN | 0.69 | open |  |
| 11-14 09:15 | +20 | ETH | DOWN | 0.69 | open |  |
| 11-14 09:15 | +15 | ETH | DOWN | 0.69 | open |  |
| 11-14 09:15 | +10 | ETH | DOWN | 0.69 | open |  |
| 11-14 09:15 | +5 | ETH | DOWN | 0.69 | 0.75 | 0.31 |
| 11-14 09:15 | +10 stop | XRP | DOWN | 0.69 | open |  |
| 11-14 09:15 | +20 | XRP | DOWN | 0.69 | open |  |
| 11-14 09:15 | +15 | XRP | DOWN | 0.69 | open |  |
| 11-14 09:15 | +10 | XRP | DOWN | 0.69 | open |  |
| 11-14 09:15 | +5 | XRP | DOWN | 0.69 | 0.74 | 0.21 |
| 11-14 09:03 | +10 stop | HYPE | UP | 0.67 | 0.83 | 1.34 |
| 11-14 09:03 | +10 stop | NEAR | UP | 0.59 | 0.69 | 0.68 |
| 11-14 09:03 | +5 | NEAR | UP | 0.58 | 0.69 | 0.77 |
| 11-14 09:02 | +10 stop | NEAR | UP | 0.50 | 0.61 | 0.75 |
| 11-14 09:02 | +5 | NEAR | UP | 0.49 | 0.59 | 0.65 |
| 11-14 09:01 | +5 | NEAR | DOWN | 0.51 | 0.60 | 0.55 |
| 11-14 09:01 | +10 stop | BNB | DOWN | 0.48 | 0.20 | -3.10 |
| 11-14 09:01 | +20 | BNB | DOWN | 0.48 | yes | -4.98 |
| 11-14 09:01 | +15 | BNB | DOWN | 0.48 | yes | -4.98 |
| 11-14 09:01 | +10 | BNB | DOWN | 0.48 | yes | -4.98 |
