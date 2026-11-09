# Range-Scalp Bot

*Updated Mon Nov 09 05:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53361 | 46525 | 6836 (85) | 1 | $-14755.57 | -4.4% |
| **+10¢** | 39857 | 31883 | 7974 (110) | 2 | $-13757.90 | -5.5% |
| **+15¢** | 33396 | 24804 | 8592 (141) | 4 | $-12562.69 | -6.0% |
| **+20¢** | 29717 | 20709 | 9008 (186) | 4 | $-11047.83 | -5.9% |
| **+10¢ (15¢ stop)** | 65026 | 64920 | 106 (63) | 1 | $-24129.38 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 05:34 | +5 | SOL | DOWN | 0.59 | 0.65 | 0.27 |
| 11-09 05:33 | +10 stop | ZEC | UP | 0.65 | 0.80 | 1.24 |
| 11-09 05:33 | +10 stop | SOL | DOWN | 0.58 | 0.70 | 0.87 |
| 11-09 05:33 | +10 | SOL | DOWN | 0.57 | 0.70 | 0.97 |
| 11-09 05:33 | +5 | SOL | DOWN | 0.57 | 0.66 | 0.56 |
| 11-09 05:32 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 11-09 05:32 | +20 | XRP | DOWN | 0.65 | open |  |
| 11-09 05:32 | +15 | XRP | DOWN | 0.65 | open |  |
| 11-09 05:32 | +10 | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-09 05:32 | +5 | XRP | DOWN | 0.65 | 0.72 | 0.39 |
| 11-09 05:32 | +10 stop | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 11-09 05:32 | +10 | HYPE | UP | 0.65 | 0.75 | 0.70 |
| 11-09 05:32 | +5 | HYPE | UP | 0.65 | 0.74 | 0.60 |
| 11-09 05:32 | +10 stop | DOGE | DOWN | 0.66 | 0.79 | 1.02 |
| 11-09 05:32 | +20 | DOGE | DOWN | 0.67 | open |  |
| 11-09 05:32 | +15 | DOGE | DOWN | 0.67 | open |  |
| 11-09 05:32 | +10 | DOGE | DOWN | 0.67 | 0.79 | 0.92 |
| 11-09 05:32 | +5 | DOGE | DOWN | 0.67 | 0.72 | 0.19 |
| 11-09 05:32 | +10 stop | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 11-09 05:32 | +20 | ETH | DOWN | 0.63 | 0.83 | 1.73 |
| 11-09 05:32 | +15 | ETH | DOWN | 0.63 | 0.80 | 1.41 |
| 11-09 05:32 | +10 | ETH | DOWN | 0.63 | 0.73 | 0.69 |
| 11-09 05:32 | +5 | ETH | DOWN | 0.64 | 0.69 | 0.18 |
| 11-09 05:32 | +10 stop | ZEC | DOWN | 0.54 | 0.35 | -2.24 |
| 11-09 05:32 | +20 | ZEC | DOWN | 0.54 | open |  |
| 11-09 05:32 | +15 | ZEC | DOWN | 0.54 | open |  |
| 11-09 05:32 | +10 | ZEC | DOWN | 0.54 | open |  |
| 11-09 05:32 | +5 | ZEC | DOWN | 0.55 | open |  |
| 11-09 05:31 | +10 stop | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-09 05:31 | +20 | SOL | DOWN | 0.61 | 0.81 | 1.72 |
| 11-09 05:31 | +15 | SOL | DOWN | 0.61 | 0.78 | 1.40 |
| 11-09 05:31 | +10 | SOL | DOWN | 0.61 | 0.71 | 0.68 |
| 11-09 05:31 | +5 | SOL | DOWN | 0.61 | 0.68 | 0.37 |
| 11-09 05:31 | +10 stop | BTC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-09 05:31 | +20 | BTC | DOWN | 0.58 | 0.78 | 1.69 |
| 11-09 05:31 | +15 | BTC | DOWN | 0.58 | 0.73 | 1.18 |
| 11-09 05:31 | +10 | BTC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-09 05:31 | +5 | BTC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-09 05:31 | +10 stop | BNB | DOWN | 0.58 | 0.71 | 0.97 |
| 11-09 05:31 | +20 | BNB | DOWN | 0.57 | 0.82 | 2.21 |
