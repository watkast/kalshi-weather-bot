# Range-Scalp Bot

*Updated Thu Nov 12 19:50 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 57194 | 49863 | 7331 (101) | 3 | $-15709.42 | -4.4% |
| **+10¢** | 42752 | 34195 | 8557 (133) | 4 | $-14653.62 | -5.5% |
| **+15¢** | 35840 | 26628 | 9212 (167) | 6 | $-13264.41 | -5.9% |
| **+20¢** | 31930 | 22265 | 9665 (217) | 8 | $-11629.75 | -5.8% |
| **+10¢ (15¢ stop)** | 69742 | 69614 | 128 (78) | 4 | $-25727.48 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 19:49 | +5 | BNB | UP | 0.65 | open |  |
| 11-12 19:49 | +10 stop | XRP | UP | 0.68 | open |  |
| 11-12 19:49 | +10 | XRP | UP | 0.68 | open |  |
| 11-12 19:49 | +5 | XRP | UP | 0.68 | open |  |
| 11-12 19:49 | +5 | SOL | UP | 0.62 | open |  |
| 11-12 19:48 | +5 | XRP | UP | 0.59 | 0.66 | 0.37 |
| 11-12 19:47 | +5 | DOGE | UP | 0.71 | 0.76 | 0.22 |
| 11-12 19:47 | +10 stop | SOL | UP | 0.63 | open |  |
| 11-12 19:47 | +20 | SOL | UP | 0.63 | open |  |
| 11-12 19:47 | +15 | SOL | UP | 0.63 | open |  |
| 11-12 19:47 | +10 | SOL | UP | 0.63 | open |  |
| 11-12 19:47 | +5 | SOL | UP | 0.63 | 0.68 | 0.17 |
| 11-12 19:47 | +10 stop | BNB | UP | 0.60 | open |  |
| 11-12 19:47 | +20 | BNB | UP | 0.60 | open |  |
| 11-12 19:47 | +15 | BNB | UP | 0.60 | open |  |
| 11-12 19:47 | +10 | BNB | UP | 0.60 | open |  |
| 11-12 19:47 | +5 | BNB | UP | 0.60 | 0.68 | 0.47 |
| 11-12 19:46 | +10 stop | XRP | UP | 0.56 | 0.66 | 0.66 |
| 11-12 19:46 | +20 | XRP | UP | 0.56 | open |  |
| 11-12 19:46 | +15 | XRP | UP | 0.56 | open |  |
| 11-12 19:46 | +10 | XRP | UP | 0.56 | 0.66 | 0.66 |
| 11-12 19:46 | +5 | XRP | UP | 0.56 | 0.63 | 0.35 |
| 11-12 19:46 | +10 stop | ETH | UP | 0.64 | 0.76 | 0.90 |
| 11-12 19:46 | +20 | ETH | UP | 0.64 | open |  |
| 11-12 19:46 | +15 | ETH | UP | 0.64 | 0.82 | 1.52 |
| 11-12 19:46 | +10 | ETH | UP | 0.64 | 0.76 | 0.90 |
| 11-12 19:46 | +5 | ETH | UP | 0.64 | 0.69 | 0.18 |
| 11-12 19:46 | +10 stop | HYPE | UP | 0.68 | 0.79 | 0.82 |
| 11-12 19:46 | +20 | HYPE | UP | 0.68 | open |  |
| 11-12 19:46 | +15 | HYPE | UP | 0.68 | open |  |
| 11-12 19:46 | +10 | HYPE | UP | 0.68 | 0.79 | 0.82 |
| 11-12 19:46 | +5 | HYPE | UP | 0.68 | 0.73 | 0.20 |
| 11-12 19:46 | +10 stop | DOGE | UP | 0.58 | 0.71 | 0.97 |
| 11-12 19:46 | +20 | DOGE | UP | 0.58 | 0.78 | 1.69 |
| 11-12 19:46 | +15 | DOGE | UP | 0.58 | 0.76 | 1.49 |
| 11-12 19:46 | +10 | DOGE | UP | 0.58 | 0.71 | 0.97 |
| 11-12 19:46 | +5 | DOGE | UP | 0.58 | 0.63 | 0.15 |
| 11-12 19:45 | +10 stop | BTC | UP | 0.68 | open |  |
| 11-12 19:45 | +20 | BTC | UP | 0.68 | open |  |
| 11-12 19:45 | +15 | BTC | UP | 0.68 | open |  |
