# Range-Scalp Bot

*Updated Sun Nov 15 22:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61315 | 53502 | 7813 (114) | 3 | $-16512.46 | -4.3% |
| **+10¢** | 45790 | 36637 | 9153 (153) | 7 | $-15500.05 | -5.4% |
| **+15¢** | 38354 | 28481 | 9873 (191) | 7 | $-14155.30 | -5.9% |
| **+20¢** | 34186 | 23828 | 10358 (243) | 7 | $-12437.01 | -5.8% |
| **+10¢ (15¢ stop)** | 74606 | 74454 | 152 (90) | 4 | $-27431.32 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 22:33 | +10 stop | BNB | UP | 0.59 | open |  |
| 11-15 22:32 | +10 stop | HYPE | UP | 0.69 | 0.84 | 1.25 |
| 11-15 22:32 | +20 | HYPE | UP | 0.68 | 0.88 | 1.76 |
| 11-15 22:32 | +15 | HYPE | UP | 0.68 | 0.84 | 1.34 |
| 11-15 22:32 | +10 | HYPE | UP | 0.68 | 0.84 | 1.34 |
| 11-15 22:32 | +5 | HYPE | UP | 0.68 | 0.73 | 0.20 |
| 11-15 22:32 | +10 stop | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 11-15 22:32 | +15 | DOGE | UP | 0.63 | open |  |
| 11-15 22:31 | +10 | DOGE | UP | 0.71 | open |  |
| 11-15 22:31 | +5 | DOGE | UP | 0.71 | open |  |
| 11-15 22:31 | +10 stop | BNB | UP | 0.69 | 0.54 | -1.83 |
| 11-15 22:31 | +20 | BNB | UP | 0.69 | open |  |
| 11-15 22:31 | +15 | BNB | UP | 0.69 | open |  |
| 11-15 22:31 | +10 | BNB | UP | 0.68 | open |  |
| 11-15 22:31 | +5 | BNB | UP | 0.67 | open |  |
| 11-15 22:31 | +10 stop | SOL | UP | 0.63 | open |  |
| 11-15 22:31 | +20 | SOL | UP | 0.63 | open |  |
| 11-15 22:31 | +15 | SOL | UP | 0.63 | open |  |
| 11-15 22:31 | +10 | SOL | UP | 0.62 | open |  |
| 11-15 22:31 | +5 | SOL | UP | 0.62 | 0.67 | 0.17 |
| 11-15 22:31 | +5 | BTC | UP | 0.62 | 0.67 | 0.17 |
| 11-15 22:31 | +10 stop | ETH | UP | 0.66 | open |  |
| 11-15 22:31 | +20 | ETH | UP | 0.67 | open |  |
| 11-15 22:31 | +15 | ETH | UP | 0.66 | open |  |
| 11-15 22:31 | +10 | ETH | UP | 0.66 | open |  |
| 11-15 22:31 | +5 | ETH | UP | 0.66 | open |  |
| 11-15 22:31 | +10 stop | DOGE | DOWN | 0.39 | 0.54 | 1.15 |
| 11-15 22:31 | +20 | DOGE | DOWN | 0.39 | open |  |
| 11-15 22:31 | +15 | DOGE | DOWN | 0.39 | 0.54 | 1.15 |
| 11-15 22:31 | +10 | DOGE | DOWN | 0.39 | 0.54 | 1.15 |
| 11-15 22:31 | +5 | DOGE | DOWN | 0.39 | 0.54 | 1.15 |
| 11-15 22:31 | +10 stop | XRP | DOWN | 0.51 | open |  |
| 11-15 22:31 | +20 | XRP | DOWN | 0.52 | open |  |
| 11-15 22:31 | +15 | XRP | DOWN | 0.52 | open |  |
| 11-15 22:31 | +10 | XRP | DOWN | 0.52 | open |  |
| 11-15 22:31 | +5 | XRP | DOWN | 0.52 | 0.58 | 0.24 |
| 11-15 22:31 | +10 stop | BTC | DOWN | 0.46 | 0.30 | -1.93 |
| 11-15 22:31 | +20 | BTC | DOWN | 0.46 | open |  |
| 11-15 22:31 | +15 | BTC | DOWN | 0.46 | open |  |
| 11-15 22:31 | +10 | BTC | DOWN | 0.46 | open |  |
