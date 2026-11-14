# Range-Scalp Bot

*Updated Sat Nov 14 23:01 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 59979 | 52315 | 7664 (107) | 0 | $-16354.06 | -4.3% |
| **+10¢** | 44818 | 35840 | 8978 (143) | 0 | $-15429.85 | -5.5% |
| **+15¢** | 37550 | 27870 | 9680 (180) | 0 | $-14073.93 | -6.0% |
| **+20¢** | 33455 | 23300 | 10155 (232) | 0 | $-12410.11 | -5.9% |
| **+10¢ (15¢ stop)** | 73009 | 72866 | 143 (82) | 0 | $-26831.10 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-14 22:52 | +10 stop | XRP | DOWN | 0.65 | 0.88 | 2.06 |
| 11-14 22:52 | +20 | XRP | DOWN | 0.65 | 0.88 | 2.06 |
| 11-14 22:52 | +10 | XRP | DOWN | 0.66 | 0.88 | 1.96 |
| 11-14 22:52 | +5 | XRP | DOWN | 0.66 | 0.88 | 1.96 |
| 11-14 22:50 | +5 | BNB | DOWN | 0.68 | 0.77 | 0.61 |
| 11-14 22:49 | +15 | XRP | DOWN | 0.63 | 0.88 | 2.25 |
| 11-14 22:49 | +10 | HYPE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-14 22:49 | +5 | HYPE | DOWN | 0.68 | 0.76 | 0.51 |
| 11-14 22:49 | +10 stop | SOL | DOWN | 0.68 | 0.78 | 0.71 |
| 11-14 22:49 | +10 stop | BTC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-14 22:49 | +5 | BTC | DOWN | 0.68 | 0.74 | 0.30 |
| 11-14 22:48 | +10 stop | BNB | DOWN | 0.62 | 0.77 | 1.20 |
| 11-14 22:48 | +10 stop | ETH | DOWN | 0.64 | 0.81 | 1.42 |
| 11-14 22:48 | +10 stop | DOGE | DOWN | 0.65 | 0.87 | 1.96 |
| 11-14 22:48 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-14 22:48 | +5 | NEAR | DOWN | 0.67 | 0.72 | 0.19 |
| 11-14 22:48 | +10 stop | SOL | UP | 0.52 | 0.36 | -1.95 |
| 11-14 22:47 | +10 stop | BNB | UP | 0.60 | 0.38 | -2.54 |
| 11-14 22:47 | +10 stop | ETH | UP | 0.60 | 0.40 | -2.34 |
| 11-14 22:47 | +20 | ETH | UP | 0.60 | no | -6.17 |
| 11-14 22:47 | +15 | ETH | UP | 0.59 | no | -6.07 |
| 11-14 22:47 | +10 | ETH | UP | 0.59 | no | -6.07 |
| 11-14 22:47 | +5 | ETH | UP | 0.60 | no | -6.17 |
| 11-14 22:47 | +10 stop | ZEC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-14 22:47 | +20 | ZEC | DOWN | 0.66 | 0.86 | 1.75 |
| 11-14 22:47 | +15 | ZEC | DOWN | 0.66 | 0.84 | 1.54 |
| 11-14 22:47 | +10 | ZEC | DOWN | 0.66 | 0.77 | 0.81 |
| 11-14 22:47 | +5 | ZEC | DOWN | 0.66 | 0.74 | 0.50 |
| 11-14 22:47 | +5 | NEAR | DOWN | 0.56 | 0.61 | 0.15 |
| 11-14 22:46 | +10 stop | BNB | DOWN | 0.61 | 0.43 | -2.15 |
| 11-14 22:46 | +20 | BNB | DOWN | 0.61 | 0.91 | 2.71 |
| 11-14 22:46 | +15 | BNB | DOWN | 0.61 | 0.77 | 1.30 |
| 11-14 22:46 | +10 | BNB | DOWN | 0.61 | 0.77 | 1.30 |
| 11-14 22:46 | +5 | BNB | DOWN | 0.61 | 0.68 | 0.37 |
| 11-14 22:46 | +10 stop | DOGE | DOWN | 0.66 | 0.43 | -2.64 |
| 11-14 22:46 | +20 | DOGE | DOWN | 0.66 | 0.87 | 1.86 |
| 11-14 22:46 | +15 | DOGE | DOWN | 0.66 | 0.87 | 1.86 |
| 11-14 22:46 | +10 | DOGE | DOWN | 0.66 | 0.87 | 1.86 |
| 11-14 22:46 | +5 | DOGE | DOWN | 0.66 | 0.74 | 0.50 |
| 11-14 22:46 | +10 | XRP | DOWN | 0.65 | 0.75 | 0.70 |
