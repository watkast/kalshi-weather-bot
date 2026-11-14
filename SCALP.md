# Range-Scalp Bot

*Updated Sat Nov 14 19:49 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59779 | 52158 | 7621 (107) | 1 | $-16172.94 | -4.3% |
| **+10¢** | 44660 | 35736 | 8924 (143) | 2 | $-15201.30 | -5.4% |
| **+15¢** | 37417 | 27794 | 9623 (180) | 5 | $-13836.35 | -5.9% |
| **+20¢** | 33334 | 23236 | 10098 (232) | 6 | $-12183.21 | -5.8% |
| **+10¢ (15¢ stop)** | 72752 | 72609 | 143 (82) | 0 | $-26750.52 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 19:47 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-14 19:47 | +20 | SOL | DOWN | 0.71 | open |  |
| 11-14 19:47 | +15 | SOL | DOWN | 0.67 | 0.87 | 1.76 |
| 11-14 19:47 | +10 | SOL | DOWN | 0.67 | 0.77 | 0.71 |
| 11-14 19:47 | +5 | SOL | DOWN | 0.68 | 0.77 | 0.61 |
| 11-14 19:47 | +10 stop | XRP | DOWN | 0.68 | 0.79 | 0.82 |
| 11-14 19:46 | +5 | NEAR | DOWN | 0.71 | 0.78 | 0.42 |
| 11-14 19:46 | +10 stop | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 11-14 19:46 | +20 | HYPE | DOWN | 0.67 | open |  |
| 11-14 19:46 | +15 | HYPE | DOWN | 0.67 | open |  |
| 11-14 19:46 | +10 | HYPE | DOWN | 0.67 | 0.80 | 1.02 |
| 11-14 19:46 | +5 | HYPE | DOWN | 0.67 | 0.73 | 0.30 |
| 11-14 19:46 | +10 stop | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 11-14 19:46 | +20 | BNB | DOWN | 0.62 | 0.83 | 1.83 |
| 11-14 19:46 | +15 | BNB | DOWN | 0.62 | 0.83 | 1.83 |
| 11-14 19:46 | +10 | BNB | DOWN | 0.62 | 0.74 | 0.89 |
| 11-14 19:46 | +5 | BNB | DOWN | 0.62 | 0.70 | 0.48 |
| 11-14 19:46 | +10 stop | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-14 19:46 | +20 | BTC | DOWN | 0.71 | open |  |
| 11-14 19:46 | +15 | BTC | DOWN | 0.71 | open |  |
| 11-14 19:46 | +10 | BTC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-14 19:46 | +5 | BTC | DOWN | 0.71 | 0.77 | 0.32 |
| 11-14 19:46 | +10 stop | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-14 19:46 | +20 | ZEC | DOWN | 0.71 | open |  |
| 11-14 19:46 | +15 | ZEC | DOWN | 0.71 | open |  |
| 11-14 19:46 | +10 | ZEC | DOWN | 0.71 | 0.82 | 0.84 |
| 11-14 19:46 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 11-14 19:46 | +10 stop | XRP | UP | 0.49 | 0.32 | -2.04 |
| 11-14 19:46 | +20 | XRP | UP | 0.49 | open |  |
| 11-14 19:46 | +15 | XRP | UP | 0.49 | open |  |
| 11-14 19:46 | +10 | XRP | UP | 0.50 | open |  |
| 11-14 19:46 | +5 | XRP | UP | 0.50 | open |  |
| 11-14 19:46 | +10 stop | NEAR | UP | 0.47 | 0.31 | -1.93 |
| 11-14 19:46 | +20 | NEAR | UP | 0.48 | open |  |
| 11-14 19:46 | +15 | NEAR | UP | 0.48 | open |  |
| 11-14 19:46 | +10 | NEAR | UP | 0.48 | open |  |
| 11-14 19:46 | +5 | NEAR | UP | 0.48 | 0.55 | 0.34 |
| 11-14 19:46 | +10 stop | ETH | DOWN | 0.62 | 0.74 | 0.89 |
| 11-14 19:46 | +20 | ETH | DOWN | 0.62 | 0.85 | 2.04 |
| 11-14 19:46 | +15 | ETH | DOWN | 0.62 | 0.78 | 1.30 |
